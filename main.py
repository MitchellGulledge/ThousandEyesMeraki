import requests
import json
import time

root_url = 'https://api.thousandeyes.com/v6'
your_email = ''
your_apikey = ''

# aid is a param for API call - target account group - required to get the right agent back if you have multiple
your_aid = '' 

# see https://developer.thousandeyes.com/v6/agents/#/agents
# note - DESPITE documentation, API does not respect the agentType param - BOOOOO!
your_optional_payload = {'agentType':'Enterprise', 'aid' : your_aid}

# get agents
def get_agents(email, api_token, payload):
    # make our Python requests module request with HTTP GET, URL, params, & basic auth
    # (see request documentation + thousandEyes URL above for details)
    te_response = requests.get(f'{ root_url }/agents.json', auth=(email, api_token), params=payload)

    # we want to convert to python dict first
    # otherwise you end up with double-encoded json (yep, I've seen this before)
    return json.loads(te_response.text)

# get agent to agent test list
def get_agent_to_agent_tests(email, api_token, payload):
    # performing get to obtain json of all agent to agent tests
    te_response = requests.get(f'{ root_url }/tests.json', auth=(email, api_token), \
        params=payload)

    # we want to convert to python dict first
    # otherwise you end up with double-encoded json (yep, I've seen this before)
    #return json.loads(te_response.text)
    return json.loads(te_response.text)

# function to create new agent to agent test with variables
def create_agent_to_agent_test(email, api_token, payload, source_agent_id, target_agent_id):

    test_payload = {"aid" : your_aid,
    "interval": 30,
        # setting protocol to UDP since we are only interested in measuring latency/loss/jitter
          "protocol": "UDP",
           "agents": [
               # source agent will be Hotel (Branch) site
             {"agentId": source_agent_id}
           ],
           # target agent will be set to one of NY area cloud servers
       "targetAgentId": target_agent_id,
           "testName": "test1"+ str(time.time()), 
           "alertsEnabled": 0
         }

    te_create_test_response = requests.put(f'{ root_url }/tests/agent-to-agent/new.json', \
        auth=(email, api_token), params=test_payload)

    return json.loads(te_create_test_response.text)
    


# call our function and we get a dict back 
te_apicall = get_agents(email=your_email, api_token=your_apikey, payload=your_optional_payload)

# te_apicall is now a dict that we can work with
# dump it to JSON (or iterate over it as a Python dict to filter by keys/values)
pretty_print = json.dumps(te_apicall, indent=4, sort_keys=False)

# creating list to iterate through to match based on country ID
agent_list = te_apicall['agents']

# creating a variable that will become list of endpoint agent IDs we want the enterprise client to hit
destination_agent_list = []

# iterating through the agent list to match all endpoints in the location New York Area
for agents in agent_list:
    # Matching all agents in the new york area on location key 
    # Filtering out IPv6 due to lack of support on Umbrella + Meraki
    if agents['location'] == 'New York Area' and 'IPv6' not in str(agents['agentName']):
        agent_id = agents['agentId']
        agent_name = agents['agentName']
        print("testing endpoint to add to list: " + str(agent_name))
        # appending agent_id to the list of destinations in destination_agent_list
        destination_agent_list.append(agent_id)

    elif agents['agentName'] == 'HotelA-PC2':
        hotel_agent_id = agents['agentId']
        hotel_agent_name = agents['agentName']
        print("Branch endpoint Name : " + str(hotel_agent_name))

    # matching all US East AWS Regions
    elif 'AWS us-east-' in str(agents['agentName']):
        aws_agent_id = agents['agentId']
        aws_agent_name = agents['agentName']
        print("AWS testing endpoint to add to list: " + str(aws_agent_name))
        # appending AWS endpoints to destination agent list
        destination_agent_list.append(aws_agent_id)

print("Current list of Destination agent IDs to test to: " + str(destination_agent_list))

# creating variable containing test IDs to delete and later create new blank slate of tests
stale_tests_to_delete = []

# Obtaining a list of current tests 
te_agent_agent_tests_apicall = get_agent_to_agent_tests(email=your_email, api_token = your_apikey, \
    payload=your_optional_payload)

print(te_agent_agent_tests_apicall)

# iterating through existing list of tests
#for tests in te_agent_agent_tests_apicall:
    #if hotel_agent_id in tests['testName']:
        #print("found")

print(time.time())

#te_agent_agent_tests_apicall = create_agent_to_agent_test(email=your_email, api_token=your_apikey, \
#    payload=your_optional_payload, source_agent_id = hotel_agent_id, target_agent_id = destination_agent_list[0]) # using first entry in dst list for now
