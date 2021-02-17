import requests
import json
from itertools import tee
import arrow
import time
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy

# creating authentication variables
root_url = 'https://api.thousandeyes.com/v6'

# fill in your email below
your_email = ''

# fill in your api key for thousandeyes, for more info on obtaining your api key:
# https://developer.thousandeyes.com/v6/
your_apikey = ''
in_mmo_agent_name = '' # fill in agent name
no_mmo_agent_name = '' # fill in agent name

# test prefix name is a variable that maps to the MMO providers name (like ATT would be ATT: )
test_prefix_name = 'PF: '

# leave these variables blank as we will map the id from the agent name listed above later
in_mmo_agent_id = ''
no_mmo_agent_id = ''

# aid is a param for API call - target account group - required to get the right agent back if you have multiple
your_aid = '199526' 

# see https://developer.thousandeyes.com/v6/agents/#/agents
# note - DESPITE documentation, API does not respect the agentType param - BOOOOO!
your_optional_payload = {'agentType':'Enterprise', 'aid' : your_aid}

# utilizing arrow library to grab current time in appropriate format, using shift method to 
# fetch last n hours, more info: https://arrow.readthedocs.io/en/stable/
test_end = arrow.utcnow().shift(hours=-48).format('YYYY-MM-DD[T]HH:mm:ss')
test_start = arrow.utcnow().shift(hours=-72).format('YYYY-MM-DD[T]HH:mm:ss')

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

# creating function to iterate through every pair of elements in a list
# more information on pairwise and zip function found here:
# https://www.semicolonworld.com/question/53790/iterate-through-pairs-of-items-in-a-python-list
# https://stackoverflow.com/questions/50239706/cannot-import-name-izip
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# get test data from test ID
def get_test_data(time_start, time_end, test_id, email, api_token):

    # creating payload to include timestamp for obtaining test data
    # time_start and time_end variables must be in the ‘YYYY-mm-ddTHH:MM:SS’ format
    test_data_payload = {'agentType':'Enterprise', 'aid' : your_aid, \
    'from' : time_start,  'to' : time_end}

    # performing get to obtain json of all agent to agent tests
    te_test_data = requests.get(f'{ root_url }/net/metrics/'+str(test_id)+'.json', \
        auth=(email, api_token), params=test_data_payload)

    # we want to convert to python dict first
    # otherwise you end up with double-encoded json (yep, I've seen this before)
    return json.loads(te_test_data.text)

# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 

# executing function to obtain list of all tests
te_test_list = get_agent_to_agent_tests(your_email, your_apikey, your_optional_payload)['test']

# utilizing list comprehension to grab all the relevant test IDs from the MMO provider
list_of_mmo_tests_in_te = [{'test_id': x['testId'], 'test_name': x['testName'], 'target_agent_id': \
    x['targetAgentId']} for x in te_test_list if test_prefix_name in x['testName'] \
        and 'MMO Test from branch to: ' in x['testName']]

# sorting the list of dictionaries by the target agent ID so we get a easy pair of 
# in MMO and No MMO tests being listed one after another, more info found here:
# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
sorted_list_of_mmo_tests = sorted(list_of_mmo_tests_in_te, key = lambda i: i['target_agent_id'])

# iterating through every pair of elements inside the sorted_list_of_mmo_tests
for v, w in pairwise(sorted_list_of_mmo_tests):

    # converting to string to slide out the first 6 characters from the name to filter out in/out mmo
    if str(v['test_name'])[6:] == str(w['test_name'])[6:]:
        #print(v)
        #print(w)
        #print("new iteration")

        # creating a temporary dictionary with lists containing the latency/loss/jitter values
        test_result_dictionary = {
            v['test_name']: {'test_latency': [], 'test_loss': [], 'test_jitter': []},
            w['test_name']: {'test_latency': [], 'test_loss': [], 'test_jitter': []}
        }

        # obtaining range of start and end times spanned at an minute and adding to the time range list
        for testing_range in arrow.Arrow.span_range('hour', arrow.get(test_start), arrow.get(test_end)):

            # executing function to obtain test information 
            v_tests_data = get_test_data(time_start = testing_range[0], time_end = testing_range[1], \
                test_id = v['test_id'], email = your_email, api_token = your_apikey)

            w_tests_data = get_test_data(time_start = testing_range[0], time_end = testing_range[1], \
                test_id = w['test_id'], email = your_email, api_token = your_apikey)

            # when tests fail in Thousandeyes they will throw a clock syncronization error, this 
            # was put in place to get around the error and continue iterating through next test ID
            if 'Clock synchronization failed' in str(v_tests_data) or \
                'Connection to target agent failed' in str(v_tests_data) or \
                    'Clock synchronization failed' in str(w_tests_data) or \
                        'Connection to target agent failed' in str(w_tests_data):

                        continue

            avg_v_latency = Average([latency['avgLatency'] for latency in v_tests_data['net']['metrics']])
            avg_w_latency = Average([latency['avgLatency'] for latency in w_tests_data['net']['metrics']])
            print(avg_v_latency)
            print(avg_w_latency)


            test_result_dictionary[v['test_name']]['test_latency'].append(avg_v_latency)

            test_result_dictionary[w['test_name']]['test_latency'].append(avg_w_latency)
           

            # sleeping 50ms to protect from rate limit
            time.sleep(.05)

        print(test_result_dictionary)

        # line 1 points 
        #x1 = numpy.array(x_length_list)
        y1 = numpy.array(test_result_dictionary[v['test_name']]['test_latency'])
        # plotting the line 2 points  
        plt.plot( y1, label = 'In VPN') 

        # line 2 points 
        #x2 = numpy.array(y_length_list)
        y2 = numpy.array(test_result_dictionary[w['test_name']]['test_latency'])
        # plotting the line 2 points  
        plt.plot( y2, label = 'No VPN') 

        # naming the x axis 
        plt.xlabel('Hours') 
        # naming the y axis 
        plt.ylabel('Latency in MS') 
        # giving a title to my graph 
        plt.title(str(v['test_name'])[6:]) 
        
        # show a legend on the plot 
        plt.legend() 
    
        # function to show the plot 
        plt.show()     

