import requests
import json
import arrow
import time
import pandas as pd 
import matplotlib.pyplot as plt 

root_url = 'https://api.thousandeyes.com/v6'
your_email = ''
your_apikey = ''
your_agentname = ''

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

# get test data from test ID
def get_test_data(time_start, time_end, test_id, email, api_token):
    # creating payload to include timestamp for obtaining test data
    # time_start and time_end variables must be in the ‘YYYY-mm-ddTHH:MM:SS’ format
    test_data_payload = {'agentType':'Enterprise', 'aid' : your_aid, \
    'from' : time_start,  'to' : time_end}
    # performing get to obtain json of all agent to agent tests
    te_test_data = requests.get(f'{ root_url }/net/metrics/'+str(test_id)+'.json', auth=(email, api_token), \
        params=test_data_payload)

    # we want to convert to python dict first
    # otherwise you end up with double-encoded json (yep, I've seen this before)
    return json.loads(te_test_data.text)

# function to remove values from a list
def remove_values_from_list(the_list, val):
    # using list comprehension to filter unwanted values
   return [value for value in the_list if value != val]


# Obtaining a list of current  agent to agent tests 
te_agent_agent_tests_apicall = get_agent_to_agent_tests(email=your_email, api_token = your_apikey, \
    payload=your_optional_payload)

# parsing the json to get to the list of dictionaries we can iterate through
List_of_tests = te_agent_agent_tests_apicall['test']

# creating a list of test IDs that match the your_agentname variable
current_list_of_agent_tests = []

# iterating through list of tests to match all tests containing the agent name
for agent in List_of_tests:
    if str(your_agentname) in str(agent['testName']):
        # since we can confirm that the agentname is inside the testname we want to append test ID to
        # the list current_list_of_agent_tests
        current_list_of_agent_tests.append(agent['testId'])

print(current_list_of_agent_tests)

# utilizing arrow library to grab current time in appropriate format
current_time = arrow.utcnow().format('YYYY-MM-DD[T]HH:mm:ss')

# statically assigning the start time of tests
tests_start = '2020-11-19T05:35:00'
tests_end = current_time

# converting from string to tz format so arrow library can obtain range
arrow_tests_start = arrow.get('2020-11-19T05:35:00')
arrow_tests_end = arrow.get(current_time)

# creating master list that stores all test dictionaries w/ timestamps
master_list_of_tests = []

# obtaining range of start and end times spanned at an hour and adding to the time range list
for testing_range in arrow.Arrow.span_range('hours', arrow_tests_start, arrow_tests_end):

    test_time_start = testing_range[0]
    test_time_end = testing_range[1]

    # iterating through list of test IDs 
    for tests in current_list_of_agent_tests:

        # executing function to obtain test information
        tests_data = get_test_data(time_start = test_time_start, time_end = test_time_end, test_id = tests, \
            email=your_email, api_token = your_apikey)

        if 'Clock synchronization failed' in str(tests_data):
            continue

        # creating variable for testname
        test_name = tests_data['net']['test']['testName']

        # creating variable for avg test latency
        test_latency = tests_data['net']['metrics'][0]['avgLatency']

        # creating variable for avg test ploss
        test_loss = tests_data['net']['metrics'][0]['loss']

        # creating variable for avg test jitter
        test_jitter = tests_data['net']['metrics'][0]['jitter']

        test_dictionary = {
            "test_name" : test_name,
            "test_latency" : test_latency,
            "test_loss" : test_loss,
            "test_jitter" : test_jitter,
            "test_start" : test_time_start.format('YYYY-MM-DD[T]HH:mm:ss'),
            "test_end" : test_time_end.format('YYYY-MM-DD[T]HH:mm:ss')
        }

        print(test_dictionary)

        # appending test_dictionary to master_list_of_tests
        master_list_of_tests.append(test_dictionary)

        # sleeping to protect from rate limit
        #time.sleep(1)

print(master_list_of_tests)

df = pd.DataFrame(master_list_of_tests) 

# saving the dataframe  
df.to_csv('ThousandEyesTest.csv')
