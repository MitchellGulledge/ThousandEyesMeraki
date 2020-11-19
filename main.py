import requests
import json

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
    return json.loads(te_response.text)


# creating function to delete stale tests
def delete_stale_tests(email, api_token, payload, test_id):
    # post to delete agent to agent tests
    te_delete_test_response = requests.post(f'{ root_url }/tests/agent-to-agent/'+ str(test_id) \
        +'/delete', auth=(email, api_token), params=payload)

    return te_delete_test_response

# function to remove values from a list
def remove_values_from_list(the_list, val):
    # using list comprehension to filter unwanted values
   return [value for value in the_list if value != val]

# function to create new agent to agent test with variables
def create_agent_to_agent_test(email, api_token, payload, body):

    te_create_test_response = requests.post(f'{ root_url }/tests/agent-to-agent/new.json', \
        auth=(email, api_token), params=payload, data = body, headers = {"Content-Type" : "application/json"})

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

# parsing the json to get to the list of dictionaries we can iterate through
List_of_tests = te_agent_agent_tests_apicall['test']

# iterating through existing list of tests
for tests in List_of_tests:
    if "Production Test" not in str(tests['testName']):
        print("detected non production test, appending to list for deletion")
        # appending the test ID for matched list to the stale_tests_to_delete variable
        stale_tests_to_delete.append(tests['testId'])
    
    # now that we have deleted all stale tests we need to create new tests if they havent been created yet
    elif "Production Test" in str(tests['testName']):
        # iterating through list of destination endpoints to test
        for agent_tests in destination_agent_list:
            if tests['targetAgentId'] == agent_tests:
                # need to remove agent ID matching tests['targetAgentId'] from destination_agent_list
                # executing function remove_values_from_list
                destination_agent_list = remove_values_from_list(destination_agent_list, \
                    tests['targetAgentId'])
                print(destination_agent_list)        

# need to iterate through list of test IDs in stale_tests_to_delete list and call the delete test api
for stale_tests in stale_tests_to_delete:
    # calling delete test function for thousandeyes
    delete_test = delete_stale_tests(email=your_email, api_token = your_apikey, \
        payload=your_optional_payload, test_id = stale_tests)
    print(delete_test)

# now that the destination_agent_list has been built and updated we can start creating tests
for new_tests in destination_agent_list:

    dst_name = ''

    # iterating through list of agents to map the new tests (equal to destination ID) to dst name
    for agent_name in agent_list:
        if new_tests == agent_name['agentId']:
            dst_name = agent_name['agentName']

    test_name = "Production Test from " + str(hotel_agent_name) + " to agent " + str(dst_name) 

    # crafting body for HTTP Post to create test in TE dashboard
    create_test_data = { "interval": 300,
        "agents": [
          {"agentId": hotel_agent_id}
        ],
        "testName": test_name,
        "targetAgentId": new_tests,
        "port": 49153,
        "alertsEnabled": 0,
      }

    print(create_test_data)

    te_agent_agent_tests_apicall = create_agent_to_agent_test(email=your_email, api_token=your_apikey, \
        payload=your_optional_payload, body = json.dumps(create_test_data)) # using first entry in dst list for now

    print(te_agent_agent_tests_apicall)
