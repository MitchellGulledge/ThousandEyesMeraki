import requests
import json
import arrow
from dateutil import tz
import time
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy

# creating thousandeyes authentication variables and root url
root_url = 'https://api.thousandeyes.com/v6'
your_email = ''
your_apikey = ''

# creating dictionary with variables for the source and destination agent names
# to parse the correct tests
test_agent_dictionary = {
    'intra_region_no_mmo_test_name' : '',
    'intra_region_in_mmo_test_name' : '',
    'inter_region_no_mmo_test_name' : '',
    'inter_region_in_mmo_test_name' : ''
    }

# aid is a param for API call - target account group - 
# required to get the right agent back if you have multiple
your_aid = '199526' 

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

# function to remove values from a list
def remove_values_from_list(the_list, val):
    # using list comprehension to filter unwanted values
   return [value for value in the_list if value != value]


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

# call our function and we get a dict back 
te_apicall = get_agent_to_agent_tests(email=your_email, api_token=your_apikey, \
    payload=your_optional_payload)

# performing list comprehension to see if the test name from the list of tests in te_apicall['test']
# we reference the values in the test_agent_dictionary, organizing as [id, name]
thousandeyes_test_ids = [[value['testId'], value['testName']] for value in te_apicall['test'] \
    if value['testName'] in test_agent_dictionary.values()]

# utilizing arrow library to grab current time in appropriate format, using shift method to 
# fetch last n hours, more info: https://arrow.readthedocs.io/en/stable/
test_end = arrow.utcnow().format('YYYY-MM-DD[T]HH:mm:ss')
test_start = arrow.utcnow().shift(hours=-18).format('YYYY-MM-DD[T]HH:mm:ss')

# creating master dictionary that we will append all the results dictionary for every nth timespan
master_test_result_dictionary = {
    test_agent_dictionary['intra_region_no_mmo_test_name'] : {'test_latency': [], 'test_loss': [], 'test_jitter': []},
    test_agent_dictionary['intra_region_in_mmo_test_name'] : {'test_latency': [], 'test_loss': [], 'test_jitter': []},
    test_agent_dictionary['inter_region_no_mmo_test_name'] : {'test_latency': [], 'test_loss': [], 'test_jitter': []},
    test_agent_dictionary['inter_region_in_mmo_test_name'] : {'test_latency': [], 'test_loss': [], 'test_jitter': []}
}

# obtaining range of start and end times spanned at an minute and adding to the time range list
for testing_range in arrow.Arrow.span_range('hour', arrow.get(test_start), arrow.get(test_end)):

    # creating variables for test start and ends
    test_time_start = testing_range[0]
    test_time_end = testing_range[1]

    # iterating through list of test IDs 
    for test_id, test_name in thousandeyes_test_ids:

        # executing function to obtain test information
        tests_data = get_test_data(time_start = test_time_start, time_end = test_time_end, \
            test_id = test_id, email = your_email, api_token = your_apikey)

        # when tests fail in Thousandeyes they will throw a clock syncronization error, this 
        # was put in place to get around the error and continue iterating through next test ID
        if 'Clock synchronization failed' in str(tests_data) or \
            'Connection to target agent failed' in str(tests_data):

            # creating dictionary for each indivdual test averages
            test_dictionary = {
                "test_name" : tests_data['net']['test']['testName'],
                "test_latency" : 0,
                "test_loss" : 0,
                "test_jitter" : 0,
                "test_start" : test_time_start.format('YYYY-MM-DD[T]HH:mm:ss'),
                "test_end" : test_time_end.format('YYYY-MM-DD[T]HH:mm:ss')
            }

            master_test_result_dictionary[test_dictionary['test_name']]['test_latency'].append(test_dictionary['test_latency'])


            continue

        # creating dictionary for each indivdual test averages
        test_dictionary = {
            "test_name" : tests_data['net']['test']['testName'],
            "test_latency" : tests_data['net']['metrics'][0]['avgLatency'],
            "test_loss" : tests_data['net']['metrics'][0]['loss'],
            "test_jitter" : tests_data['net']['metrics'][0]['jitter'],
            "test_start" : test_time_start.format('YYYY-MM-DD[T]HH:mm:ss'),
            "test_end" : test_time_end.format('YYYY-MM-DD[T]HH:mm:ss')
        }

        # appending test dictionary latency to list within master results dictionary so we can later 
        # graph the results with matplotlib
        master_test_result_dictionary[test_dictionary['test_name']]['test_latency'].append(test_dictionary['test_latency'])

        # appending test_dictionary to master_list_of_tests

        # sleeping 500ms to protect from rate limit
        time.sleep(.5)


#print(master_test_result_dictionary)

    
print(master_test_result_dictionary[test_agent_dictionary['inter_region_no_mmo_test_name']]['test_latency'])
print(master_test_result_dictionary[test_agent_dictionary['inter_region_in_mmo_test_name']]['test_latency'])



def get_latency_plot_graph():
    
    # line 1 points 
    #x1 = numpy.array(x_length_list)
    y1 = numpy.array(master_test_result_dictionary[test_agent_dictionary['inter_region_no_mmo_test_name']]['test_latency'])
    # plotting the line 2 points  
    plt.plot( y1, label = "No Middle Mile") 




    # line 2 points 
    #x2 = numpy.array(y_length_list)
    y2 = numpy.array(master_test_result_dictionary[test_agent_dictionary['inter_region_in_mmo_test_name']]['test_latency'])
    # plotting the line 2 points  
    plt.plot( y2, label = "In Middle Mile") 

    # naming the x axis 
    plt.xlabel('Hours') 
    # naming the y axis 
    plt.ylabel('Latency in MS') 
    # giving a title to my graph 
    plt.title('Latency Difference Between No VPN and VPN') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 

get_latency_plot_graph()
