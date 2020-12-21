import csv
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
# importing mean() 
from statistics import mean 

# defining function to calculate mean of a list
def Average(lst): 
    return mean(lst)

test_avg_name_list = ['No VPN LAX TE' , 'No VPN ATT' , 'No VPN Level3', 'No VPN Charter', 'No VPN Comcast', 
        'No VPN Cox', 'No VPN GCP West 2', 'No VPN Verizon', 'No VPN AWS West 1', 'No VPN Alibaba US West 1',
            'No VPN AWS West US 2' , 'In VPN LAX TE' , 'In VPN ATT' , 'In VPN Level3', 'In VPN Charter', 'In VPN Comcast',
                'In VPN Cox', 'In VPN GCP West 2', 'In VPN Verizon', 'In VPN AWS West 1', 'In VPN Alibaba US West 1',
                    'In VPN AWS West US 2']

# opening CSV file that contains all tests and converting to pandas df
df_greg_raw_test_csv = pd.read_csv('first-csv-filename.csv', index_col=0)

# opening CSV file that contains all tests and converting to pandas df
df_greg_sigraki_test_csv = pd.read_csv('second-csv-filename.csv', index_col=0)

# set of lists for latency for each test (no vpn)
raw_lax_latency = []
raw_att_lax_latency = []
raw_level3_lax_latency = []
raw_charter_lax_latency = []
raw_comcast_lax_latency = []
raw_cox_lax_latency = []
raw_gcp_us_west_2_latency = []
raw_verizon_lax_latency = []
raw_aws_us_west_1_latency = []
raw_alibaba_us_west_1_latency = []
raw_aws_us_west_2_latency = []

# set of lists for latency for each test (in vpn)
vpn_lax_latency = []
vpn_att_lax_latency = []
vpn_level3_lax_latency = []
vpn_charter_lax_latency = []
vpn_comcast_lax_latency = []
vpn_cox_lax_latency = []
vpn_gcp_us_west_2_latency = []
vpn_verizon_lax_latency = []
vpn_aws_us_west_1_latency = []
vpn_alibaba_us_west_1_latency = []
vpn_aws_us_west_2_latency = []

# set of lists for loss for each test (no vpn)
raw_lax_loss = []
raw_att_lax_loss = []
raw_level3_lax_loss = []
raw_charter_lax_loss = []
raw_comcast_lax_loss = []
raw_cox_lax_loss = []
raw_gcp_us_west_2_loss = []
raw_verizon_lax_loss = []
raw_aws_us_west_1_loss = []
raw_alibaba_us_west_1_loss = []
raw_aws_us_west_2_loss = []

# set of lists for loss for each test (in vpn)
vpn_lax_loss = []
vpn_att_lax_loss = []
vpn_level3_lax_loss = []
vpn_charter_lax_loss = []
vpn_comcast_lax_loss = []
vpn_cox_lax_loss = []
vpn_gcp_us_west_2_loss = []
vpn_verizon_lax_loss = []
vpn_aws_us_west_1_loss = []
vpn_alibaba_us_west_1_loss = []
vpn_aws_us_west_2_loss = []

# set of lists for jitter for each test (no vpn)
raw_lax_jitter = []
raw_att_lax_jitter = []
raw_level3_lax_jitter = []
raw_charter_lax_jitter = []
raw_comcast_lax_jitter = []
raw_cox_lax_jitter = []
raw_gcp_us_west_2_jitter = []
raw_verizon_lax_jitter = []
raw_aws_us_west_1_jitter = []
raw_alibaba_us_west_1_jitter = []
raw_aws_us_west_2_jitter = []

# set of lists for jitter for each test (in vpn)
vpn_lax_jitter = []
vpn_att_lax_jitter = []
vpn_level3_lax_jitter = []
vpn_charter_lax_jitter = []
vpn_comcast_lax_jitter = []
vpn_cox_lax_jitter = []
vpn_gcp_us_west_2_jitter = []
vpn_verizon_lax_jitter = []
vpn_aws_us_west_1_jitter = []
vpn_alibaba_us_west_1_jitter = []
vpn_aws_us_west_2_jitter = []

# set of lists for test starts for each test (no vpn)
raw_lax_test_start = []
raw_att_lax_test_start = []
raw_level3_lax_test_start = []
raw_charter_lax_test_start = []
raw_comcast_lax_test_start = []
raw_cox_lax_test_start = []
raw_gcp_us_west_2_test_start = []
raw_verizon_lax_test_start = []
raw_aws_us_west_1_test_start = []
raw_alibaba_us_west_1_test_start = []
raw_aws_us_west_2_test_start = []

# set of lists for test starts for each test (in vpn)
vpn_lax_test_start = []
vpn_att_lax_test_start = []
vpn_level3_lax_test_start = []
vpn_charter_lax_test_start = []
vpn_comcast_lax_test_start = []
vpn_cox_lax_test_start = []
vpn_gcp_us_west_2_test_start = []
vpn_verizon_lax_test_start = []
vpn_aws_us_west_1_test_start = []
vpn_alibaba_us_west_1_test_start = []
vpn_aws_us_west_2_test_start = []

# creating placeholder variables so we can create values for the x axis
vpn_lax_rows = []
vpn_att_lax_rows = []
vpn_level3_lax_rows = []
vpn_charter_lax_rows = []
vpn_comcast_lax_rows = []
vpn_cox_lax_rows = []
vpn_gcp_us_west_2_rows = []
vpn_verizon_lax_rows = []
vpn_aws_us_west_1_rows = []
vpn_alibaba_us_west_1_rows = []
vpn_aws_us_west_2_rows = []

raw_lax_rows = []
raw_att_lax_rows = []
raw_level3_lax_rows = []
raw_charter_lax_rows = []
raw_comcast_lax_rows = []
raw_cox_lax_rows = []
raw_gcp_us_west_2_rows = []
raw_verizon_lax_rows = []
raw_aws_us_west_1_rows = []
raw_alibaba_us_west_1_rows = []
raw_aws_us_west_2_rows = []

# creating placeholder variables so we can create values for the x axis
vpn_lax_row = 1
vpn_att_lax_row = 1
vpn_level3_lax_row = 1
vpn_charter_lax_row = 1
vpn_comcast_lax_row = 1
vpn_cox_lax_row = 1
vpn_gcp_us_west_2_row = 1
vpn_verizon_lax_row = 1
vpn_aws_us_west_1_row = 1
vpn_alibaba_us_west_1_row = 1
vpn_aws_us_west_2_row = 1

raw_lax_row = 1
raw_att_lax_row = 1
raw_level3_lax_row = 1
raw_charter_lax_row = 1
raw_comcast_lax_row = 1
raw_cox_lax_row = 1
raw_gcp_us_west_2_row = 1
raw_verizon_lax_row = 1
raw_aws_us_west_1_row = 1
raw_alibaba_us_west_1_row = 1
raw_aws_us_west_2_row = 1

# iterating through df_raw_test_csv to build the three sublists for the three separate graphs
for index, row in df_greg_raw_test_csv.iterrows():

    # if statement that matches test name and appends metrics (latency/loss/jitter) to appropriate list
    if "Los Angeles, CA (AT&T)" in str(row['test_name']):

        raw_att_lax_latency.append(row['test_latency'])
        raw_att_lax_loss.append(row['test_loss'])
        raw_att_lax_jitter.append(row['test_jitter'])
        raw_att_lax_test_start.append(row['test_start'])

        raw_att_lax_rows.append(raw_att_lax_row)

        raw_att_lax_row = raw_att_lax_row + 1

    elif "Los Angeles, CA (CenturyLink)" in str(row['test_name']):

        raw_level3_lax_latency.append(row['test_latency'])
        raw_level3_lax_loss.append(row['test_loss'])
        raw_level3_lax_jitter.append(row['test_jitter'])
        raw_level3_lax_test_start.append(row['test_start'])

        raw_level3_lax_rows.append(raw_level3_lax_row)

        raw_level3_lax_row = raw_level3_lax_row + 1

    elif "Los Angeles, CA (Charter)" in str(row['test_name']):

        raw_charter_lax_latency.append(row['test_latency'])
        raw_charter_lax_loss.append(row['test_loss'])
        raw_charter_lax_jitter.append(row['test_jitter'])
        raw_charter_lax_test_start.append(row['test_start'])

        raw_charter_lax_rows.append(raw_charter_lax_row)

        raw_charter_lax_row = raw_charter_lax_row + 1

    elif "Los Angeles, CA (Comcast)" in str(row['test_name']):
        
        raw_comcast_lax_latency.append(row['test_latency'])
        raw_comcast_lax_loss.append(row['test_loss'])
        raw_comcast_lax_jitter.append(row['test_jitter'])
        raw_comcast_lax_test_start.append(row['test_start'])

        raw_comcast_lax_rows.append(raw_comcast_lax_row)

        raw_comcast_lax_row = raw_comcast_lax_row + 1

    elif "Los Angeles, CA (Cox)" in str(row['test_name']):

        raw_cox_lax_latency.append(row['test_latency'])
        raw_cox_lax_loss.append(row['test_loss'])
        raw_cox_lax_jitter.append(row['test_jitter'])
        raw_cox_lax_test_start.append(row['test_start'])

        raw_cox_lax_rows.append(raw_cox_lax_row)

        raw_cox_lax_row = raw_cox_lax_row + 1

    elif "Los Angeles, CA (GCP us-west2)" in str(row['test_name']):

        raw_gcp_us_west_2_latency.append(row['test_latency'])
        raw_gcp_us_west_2_loss.append(row['test_loss'])
        raw_gcp_us_west_2_jitter.append(row['test_jitter'])
        raw_gcp_us_west_2_test_start.append(row['test_start'])

        raw_gcp_us_west_2_rows.append(raw_gcp_us_west_2_row)

        raw_gcp_us_west_2_row = raw_gcp_us_west_2_row + 1

    elif "Los Angeles, CA (Verizon)" in str(row['test_name']):

        raw_verizon_lax_latency.append(row['test_latency'])
        raw_verizon_lax_loss.append(row['test_loss'])
        raw_verizon_lax_jitter.append(row['test_jitter'])
        raw_verizon_lax_test_start.append(row['test_start'])

        raw_verizon_lax_rows.append(raw_verizon_lax_row)

        raw_verizon_lax_row = raw_verizon_lax_row + 1

    elif "San Jose, CA (AWS us-west-1)" in str(row['test_name']):

        raw_aws_us_west_1_latency.append(row['test_latency'])
        raw_aws_us_west_1_loss.append(row['test_loss'])
        raw_aws_us_west_1_jitter.append(row['test_jitter'])
        raw_aws_us_west_1_test_start.append(row['test_start'])

        raw_aws_us_west_1_rows.append(raw_aws_us_west_1_row)

        raw_aws_us_west_1_row = raw_aws_us_west_1_row + 1

    elif "Silicon Valley (Alibaba us-west-1)" in str(row['test_name']):

        raw_alibaba_us_west_1_latency.append(row['test_latency'])
        raw_alibaba_us_west_1_loss.append(row['test_loss'])
        raw_alibaba_us_west_1_jitter.append(row['test_jitter'])
        raw_alibaba_us_west_1_test_start.append(row['test_start'])

        raw_alibaba_us_west_1_rows.append(raw_alibaba_us_west_1_row)

        raw_alibaba_us_west_1_row = raw_alibaba_us_west_1_row + 1

    elif "The Dalles, OR (AWS us-west-2)" in str(row['test_name']):

        raw_aws_us_west_2_latency.append(row['test_latency'])
        raw_aws_us_west_2_loss.append(row['test_loss'])
        raw_aws_us_west_2_jitter.append(row['test_jitter'])
        raw_aws_us_west_2_test_start.append(row['test_start'])

        raw_aws_us_west_2_rows.append(raw_aws_us_west_2_row)

        raw_aws_us_west_2_row = raw_aws_us_west_2_row + 1

    elif "Los Angeles, CA" in str(row['test_name']):

        raw_lax_latency.append(row['test_latency'])
        raw_lax_loss.append(row['test_loss'])
        raw_lax_jitter.append(row['test_jitter'])
        raw_lax_test_start.append(row['test_start'])

        raw_lax_rows.append(raw_lax_row)

        raw_lax_row = raw_lax_row + 1
    

# iterating through df_raw_test_csv to build the three sublists for the three separate graphs
for index, row in df_greg_sigraki_test_csv.iterrows():

    # if statement that matches test name and appends metrics (latency/loss/jitter) to appropriate list
    if "Los Angeles, CA (AT&T)" in str(row['test_name']):

        vpn_att_lax_latency.append(row['test_latency'])
        vpn_att_lax_loss.append(row['test_loss'])
        vpn_att_lax_jitter.append(row['test_jitter'])
        vpn_att_lax_test_start.append(row['test_start'])

        vpn_att_lax_rows.append(vpn_att_lax_row)

        vpn_att_lax_row = vpn_att_lax_row + 1

    elif "Los Angeles, CA (CenturyLink)" in str(row['test_name']):

        vpn_level3_lax_latency.append(row['test_latency'])
        vpn_level3_lax_loss.append(row['test_loss'])
        vpn_level3_lax_jitter.append(row['test_jitter'])
        vpn_level3_lax_test_start.append(row['test_start'])

        vpn_level3_lax_rows.append(vpn_level3_lax_row)

        vpn_level3_lax_row = vpn_level3_lax_row + 1

    elif "Los Angeles, CA (Charter)" in str(row['test_name']):

        vpn_charter_lax_latency.append(row['test_latency'])
        vpn_charter_lax_loss.append(row['test_loss'])
        vpn_charter_lax_jitter.append(row['test_jitter'])
        vpn_charter_lax_test_start.append(row['test_start'])

        vpn_charter_lax_rows.append(vpn_charter_lax_row)

        vpn_charter_lax_row = vpn_charter_lax_row + 1

    elif "Los Angeles, CA (Comcast)" in str(row['test_name']):
        
        vpn_comcast_lax_latency.append(row['test_latency'])
        vpn_comcast_lax_loss.append(row['test_loss'])
        vpn_comcast_lax_jitter.append(row['test_jitter'])
        vpn_comcast_lax_test_start.append(row['test_start'])

        vpn_comcast_lax_rows.append(vpn_comcast_lax_row)

        vpn_comcast_lax_row = vpn_comcast_lax_row + 1

    elif "Los Angeles, CA (Cox)" in str(row['test_name']):

        vpn_cox_lax_latency.append(row['test_latency'])
        vpn_cox_lax_loss.append(row['test_loss'])
        vpn_cox_lax_jitter.append(row['test_jitter'])
        vpn_cox_lax_test_start.append(row['test_start'])

        vpn_cox_lax_rows.append(vpn_cox_lax_row)

        vpn_cox_lax_row = vpn_cox_lax_row + 1

    elif "Los Angeles, CA (GCP us-west2)" in str(row['test_name']):

        vpn_gcp_us_west_2_latency.append(row['test_latency'])
        vpn_gcp_us_west_2_loss.append(row['test_loss'])
        vpn_gcp_us_west_2_jitter.append(row['test_jitter'])
        vpn_gcp_us_west_2_test_start.append(row['test_start'])

        vpn_gcp_us_west_2_rows.append(vpn_gcp_us_west_2_row)

        vpn_gcp_us_west_2_row = vpn_gcp_us_west_2_row + 1

    elif "Los Angeles, CA (Verizon)" in str(row['test_name']):

        vpn_verizon_lax_latency.append(row['test_latency'])
        vpn_verizon_lax_loss.append(row['test_loss'])
        vpn_verizon_lax_jitter.append(row['test_jitter'])
        vpn_verizon_lax_test_start.append(row['test_start'])

        vpn_verizon_lax_rows.append(vpn_verizon_lax_row)

        vpn_verizon_lax_row = vpn_verizon_lax_row + 1

    elif "San Jose, CA (AWS us-west-1)" in str(row['test_name']):

        vpn_aws_us_west_1_latency.append(row['test_latency'])
        vpn_aws_us_west_1_loss.append(row['test_loss'])
        vpn_aws_us_west_1_jitter.append(row['test_jitter'])
        vpn_aws_us_west_1_test_start.append(row['test_start'])

        vpn_aws_us_west_1_rows.append(vpn_aws_us_west_1_row)

        vpn_aws_us_west_1_row = vpn_aws_us_west_1_row + 1

    elif "Silicon Valley (Alibaba us-west-1)" in str(row['test_name']):

        vpn_alibaba_us_west_1_latency.append(row['test_latency'])
        vpn_alibaba_us_west_1_loss.append(row['test_loss'])
        vpn_alibaba_us_west_1_jitter.append(row['test_jitter'])
        vpn_alibaba_us_west_1_test_start.append(row['test_start'])

        vpn_alibaba_us_west_1_rows.append(vpn_alibaba_us_west_1_row)

        vpn_alibaba_us_west_1_row = vpn_alibaba_us_west_1_row + 1

    elif "The Dalles, OR (AWS us-west-2)" in str(row['test_name']):

        vpn_aws_us_west_2_latency.append(row['test_latency'])
        vpn_aws_us_west_2_loss.append(row['test_loss'])
        vpn_aws_us_west_2_jitter.append(row['test_jitter'])
        vpn_aws_us_west_2_test_start.append(row['test_start'])

        vpn_aws_us_west_2_rows.append(vpn_aws_us_west_2_row)

        vpn_aws_us_west_2_row = vpn_aws_us_west_2_row + 1

    elif "Los Angeles, CA" in str(row['test_name']):

        vpn_lax_latency.append(row['test_latency'])
        vpn_lax_loss.append(row['test_loss'])
        vpn_lax_jitter.append(row['test_jitter'])
        vpn_lax_test_start.append(row['test_start'])

        vpn_lax_rows.append(vpn_lax_row)

        vpn_lax_row = vpn_lax_row + 1








def get_latency_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_latency)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Latency") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Latency") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Latency") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Latency") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Latency") 

    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Latency") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_latency)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Latency") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Latency") 

    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 2 Latency") 

    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Latency") 

    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Latency") 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_latency)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Latency") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Latency") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Latency") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Latency") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Latency") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Latency") 

    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Latency") 

    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Latency") 

    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 2 Latency") 

    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Latency") 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Latency") 











    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter graph') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 

#get_latency_plot_graph()





def get_cloud_latency_plot_graph():
    
    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Latency") 


    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 2 Latency") 

    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Latency") 

    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Latency") 


    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Latency") 


    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 2 Latency") 

    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Latency") 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Latency") 



    # naming the x axis 
    plt.xlabel('units in time beginning from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across All Cloud Service Providers') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 


def get_aws_latency_plot_graph():


    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 1 Latency", color = 'blue') 


    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Latency", color = 'orange') 



    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 1 Latency", color = 'navy') 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Latency", color = 'red') 




    # naming the x axis 
    plt.xlabel('units in time from beginning of test period to the end') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across All AWS Endpoints In and Out of VPN') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 


def get_gcp_latency_plot_graph():
    
    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Latency") 




    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Latency") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Difference Between No VPN and VPN for GCP') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 



def get_alicloud_latency_plot_graph():
    

    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Latency") 





    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_latency)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Latency") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Difference Between No VPN and VPN for AliCloud') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 


def get_isp_latency_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_latency)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Latency") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Latency") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Latency") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Latency") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Latency") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_latency)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Latency") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Latency") 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_latency)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Latency") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Latency") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Latency") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Latency") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Latency") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Latency") 


    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Latency") 





    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across all Internet Service Providers​') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_isp_no_vpn_latency_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_latency)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Latency") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Latency") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Latency") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Latency") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Latency") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_latency)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Latency") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Latency") 



    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across all ISPs No VPN') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 





def get_isp_with_sigraki_latency_plot_graph():



    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_latency)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Latency") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_latency)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Latency") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Latency") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Latency") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Latency") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Latency") 


    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Latency") 





    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across all ISPs With SIGraki​') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 





def get_isp_latency_plot_graph_no_att():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_latency)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Latency") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Latency") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Latency") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Latency") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_latency)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Latency") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Latency") 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_latency)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Latency") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_latency)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Latency") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_latency)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Latency") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_latency)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Latency") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_latency)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Latency") 


    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_latency)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Latency") 





    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Latency from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Latency Across All ISPs Excluding ATT') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_loss_csp_plot_graph():

   

    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Loss") 



    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_loss)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 1 Loss") 

    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_loss)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Loss") 

    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Loss") 




    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Loss") 

    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_loss)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 2 Loss") 

    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_loss)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Loss") 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Loss") 



    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Packet Loss from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Packet Loss Across All Cloud Service Provider Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_isp_loss_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_loss)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Loss") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_loss)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Loss") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_loss)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Loss") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_loss)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Loss") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_loss)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Loss") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_loss)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Loss") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_loss)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Loss") 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_loss)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Loss") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_loss)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Loss") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_loss)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Loss") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_loss)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Loss") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_loss)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Loss") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Loss") 


    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_loss)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Loss") 





    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Packet Loss from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Packet Loss Graph Across All Internet Service Provider Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_in_vpn_isp_loss_plot_graph():


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_loss)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Loss") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_loss)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Loss") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_loss)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Loss") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_loss)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Loss") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_loss)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Loss") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_loss)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Loss") 


    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_loss)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Loss") 





    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Packet Loss from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Packet Loss Graph Across All Internet Service Provider Endpoints Using SIGraki') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_no_vpn_isp_loss_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_loss)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Loss") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_loss)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Loss") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_loss)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 Loss") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_loss)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Loss") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_loss)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Loss") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_loss)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Loss") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_loss)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Loss") 








    # naming the x axis 
    plt.xlabel('units in time from 12/05 to 12/19') 
    # naming the y axis 
    plt.ylabel('Packet Loss from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Packet Loss Graph Across All Internet Service Provider Endpoints not using SIGraki') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 



def get_isp_jitter_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_jitter)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Jitter") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Jitter") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 jitter") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Jitter") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Jitter") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Jitter") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Jitter") 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_jitter)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Jitter") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Jitter") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Jitter") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Jitter") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Jitter") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Jitter") 

    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Jitter") 





    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter For All ISP Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 


def get_no_vpn_isp_jitter_plot_graph():
    # line 1 points 
    x1 = np.array(raw_lax_rows)
    y1 = np.array(raw_lax_jitter)
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "No VPN TE General Jitter") 
    
    # line 2 points 
    x2 = np.array(raw_att_lax_rows)
    y2 = np.array(raw_att_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "No VPN ATT Jitter") 

    # line 3 points 
    x3 = np.array(raw_level3_lax_rows)
    y3 = np.array(raw_level3_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x3, y3, label = "No VPN Level3 jitter") 

    # line 4 points 
    x4 = np.array(raw_charter_lax_rows)
    y4 = np.array(raw_charter_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x4, y4, label = "No VPN Charter Jitter") 

    # line 5 points 
    x5 = np.array(raw_comcast_lax_rows)
    y5 = np.array(raw_comcast_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x5, y5, label = "No VPN Comcast Jitter") 

    # line 7 points 
    x7 = np.array(raw_cox_lax_rows)
    y7 = np.array(raw_cox_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x7, y7, label = "No VPN Cox Jitter") 

    # line 8 points 
    x8 = np.array(raw_verizon_lax_rows)
    y8 = np.array(raw_verizon_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x8, y8, label = "No VPN Verizon Jitter") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter For All ISP Endpoints Without VPN') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 





def get_cloud_jitter_plot_graph():


    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Jitter") 



    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 2 Jitter") 

    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Jitter") 

    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Jitter") 


    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Jitter") 

    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 2 Jitter") 

    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Jitter") 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Jitter") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter Across All Cloud Providers') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show()






def get_aws_jitter_plot_graph():



    # line 9 points 
    x9 = np.array(raw_aws_us_west_1_rows)
    y9 = np.array(raw_aws_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x9, y9, label = "No VPN AWS US West 1 Jitter") 

    # line 11 points 
    x11 = np.array(raw_aws_us_west_2_rows)
    y11 = np.array(raw_aws_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x11, y11, label = "No VPN AWS West 2 Jitter") 

    # line 20 points 
    x20 = np.array(vpn_aws_us_west_1_rows)
    y20 = np.array(vpn_aws_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x20, y20, label = "In VPN AWS US West 1 Jitter") 

    # line 22 points 
    x22 = np.array(vpn_aws_us_west_2_rows)
    y22 = np.array(vpn_aws_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x22, y22, label = "In VPN AWS West 2 Jitter") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter Across AWS Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show()



def get_gcp_jitter_plot_graph():


    # line 6 points 
    x6 = np.array(raw_gcp_us_west_2_rows)
    y6 = np.array(raw_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x6, y6, label = "No VPN GCP US West 2 Jitter") 


    # line 18 points 
    x18 = np.array(vpn_gcp_us_west_2_rows)
    y18 = np.array(vpn_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x18, y18, label = "In VPN GCP US West 2 Jitter") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter Across GCP Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show()



def get_alicloud_jitter_plot_graph():


    # line 10 points 
    x10 = np.array(raw_alibaba_us_west_1_rows)
    y10 = np.array(raw_alibaba_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x10, y10, label = "No VPN Alibaba US West 1 Jitter") 

    # line 21 points 
    x21 = np.array(vpn_alibaba_us_west_1_rows)
    y21 = np.array(vpn_alibaba_us_west_1_jitter)
    # plotting the line 2 points  
    plt.plot(x21, y21, label = "In VPN Alibaba US West 1 Jitter") 



    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter Across Alicloud Endpoints') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show()





def get_with_vpn_isp_jitter_plot_graph():
 


    # line 12 points 
    x12 = np.array(vpn_lax_rows)
    y12 = np.array(vpn_lax_jitter)
    # plotting the line 1 points  
    plt.plot(x12, y12, label = "In VPN TE General Jitter") 
    
    # line 13 points 
    x13 = np.array(vpn_att_lax_rows)
    y13 = np.array(vpn_att_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x13, y13, label = "In VPN ATT Jitter") 

    # line 14 points 
    x14 = np.array(vpn_level3_lax_rows)
    y14 = np.array(vpn_level3_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x14, y14, label = "In VPN Level3 Jitter") 

    # line 15 points 
    x15 = np.array(vpn_charter_lax_rows)
    y15 = np.array(vpn_charter_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x15, y15, label = "In VPN Charter Jitter") 

    # line 16 points 
    x16 = np.array(vpn_comcast_lax_rows)
    y16 = np.array(vpn_comcast_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x16, y16, label = "In VPN Comcast Jitter") 

    # line 17 points 
    x17 = np.array(vpn_gcp_us_west_2_rows)
    y17 = np.array(vpn_gcp_us_west_2_jitter)
    # plotting the line 2 points  
    plt.plot(x17, y17, label = "In VPN Cox Jitter") 

    # line 19 points 
    x19 = np.array(vpn_verizon_lax_rows)
    y19 = np.array(vpn_verizon_lax_jitter)
    # plotting the line 2 points  
    plt.plot(x19, y19, label = "In VPN Verizon Jitter") 


    # naming the x axis 
    plt.xlabel('units in time') 
    # naming the y axis 
    plt.ylabel('Jitter from agent on prem to enterprise cloud agent') 
    # giving a title to my graph 
    plt.title('Jitter For All ISP Endpoints with VPN') 
    
    # show a legend on the plot 
    plt.legend() 
    
    # function to show the plot 
    plt.show() 




def get_latency_averages():
    latency_performance_list = [float(Average(raw_lax_latency)), float(Average(raw_att_lax_latency)), 
        float(Average(raw_level3_lax_latency)), float(Average(raw_charter_lax_latency)), 
            float(Average(raw_comcast_lax_latency)), float(Average(raw_cox_lax_latency)), 
                float(Average(raw_gcp_us_west_2_latency)), float(Average(raw_verizon_lax_latency)), 
                    float(Average(raw_aws_us_west_1_latency)), float(Average(raw_alibaba_us_west_1_latency)), 
                        float(Average(raw_aws_us_west_2_latency)), float(Average(vpn_lax_latency)), 
                            float(Average(vpn_att_lax_latency)), float(Average(vpn_level3_lax_latency)), 
                                float(Average(vpn_charter_lax_latency)), float(Average(vpn_comcast_lax_latency)), 
                                    float(Average(vpn_cox_lax_latency)), float(Average(vpn_gcp_us_west_2_latency)), 
                                        float(Average(vpn_verizon_lax_latency)), float(Average(vpn_aws_us_west_1_latency)), 
                                            float(Average(vpn_alibaba_us_west_1_latency)), 
                                                float(Average(vpn_aws_us_west_2_latency))]



    print(latency_performance_list)


    in_vpn_means = [float(Average(vpn_lax_latency)), 
                            float(Average(vpn_att_lax_latency)), float(Average(vpn_level3_lax_latency)), 
                                float(Average(vpn_charter_lax_latency)), float(Average(vpn_comcast_lax_latency)), 
                                    float(Average(vpn_cox_lax_latency)), float(Average(vpn_gcp_us_west_2_latency)), 
                                        float(Average(vpn_verizon_lax_latency)), float(Average(vpn_aws_us_west_1_latency)), 
                                            float(Average(vpn_alibaba_us_west_1_latency)), 
                                                float(Average(vpn_aws_us_west_2_latency))]

    no_vpn_means = [float(Average(raw_lax_latency)), float(Average(raw_att_lax_latency)), 
        float(Average(raw_level3_lax_latency)), float(Average(raw_charter_lax_latency)), 
            float(Average(raw_comcast_lax_latency)), float(Average(raw_cox_lax_latency)), 
                float(Average(raw_gcp_us_west_2_latency)), float(Average(raw_verizon_lax_latency)), 
                    float(Average(raw_aws_us_west_1_latency)), float(Average(raw_alibaba_us_west_1_latency)), 
                        float(Average(raw_aws_us_west_2_latency))]

    print(test_avg_name_list)
    print(latency_performance_list)


    labels = ['TE', 'ATT', 'Level3', 'Charter', 'Comcast', 'Cox', 'GCP West 2', 'Verizon', 'AWS West 1', 'Alibaba West 1', 'AWS West 2']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, in_vpn_means, width, label='In VPN')
    rects2 = ax.bar(x + width/2, no_vpn_means, width, label='No VPN')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Latency Averages')
    ax.set_title('Latency Differences Across All 11 Endpoints')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = int(rect.get_height())
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()



def get_loss_averages():


    in_vpn_means = [float(Average(vpn_lax_loss)), 
                            float(Average(vpn_att_lax_loss)), float(Average(vpn_level3_lax_loss)), 
                                float(Average(vpn_charter_lax_loss)), float(Average(vpn_comcast_lax_loss)), 
                                    float(Average(vpn_cox_lax_loss)), float(Average(vpn_gcp_us_west_2_loss)), 
                                        float(Average(vpn_verizon_lax_loss)), float(Average(vpn_aws_us_west_1_loss)), 
                                            float(Average(vpn_alibaba_us_west_1_loss)), 
                                                float(Average(vpn_aws_us_west_2_loss))]

    no_vpn_means = [float(Average(raw_lax_loss)), float(Average(raw_att_lax_loss)), 
        float(Average(raw_level3_lax_loss)), float(Average(raw_charter_lax_loss)), 
            float(Average(raw_comcast_lax_loss)), float(Average(raw_cox_lax_loss)), 
                float(Average(raw_gcp_us_west_2_loss)), float(Average(raw_verizon_lax_loss)), 
                    float(Average(raw_aws_us_west_1_loss)), float(Average(raw_alibaba_us_west_1_loss)), 
                        float(Average(raw_aws_us_west_2_loss))]


    labels = ['TE', 'ATT', 'Level3', 'Charter', 'Comcast', 'Cox', 'GCP West 2', 'Verizon', 'AWS West 1', 'Alibaba West 1', 'AWS West 2']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, in_vpn_means, width, label='In VPN')
    rects2 = ax.bar(x + width/2, no_vpn_means, width, label='No VPN')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Loss Averages')
    ax.set_title('Loss Differences Across All 11 Endpoints')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = int(rect.get_height())
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()


def get_jitter_averages():


    in_vpn_means = [float(Average(vpn_lax_jitter)), 
                            float(Average(vpn_att_lax_jitter)), float(Average(vpn_level3_lax_jitter)), 
                                float(Average(vpn_charter_lax_jitter)), float(Average(vpn_comcast_lax_jitter)), 
                                    float(Average(vpn_cox_lax_jitter)), float(Average(vpn_gcp_us_west_2_jitter)), 
                                        float(Average(vpn_verizon_lax_jitter)), float(Average(vpn_aws_us_west_1_jitter)), 
                                            float(Average(vpn_alibaba_us_west_1_jitter)), 
                                                float(Average(vpn_aws_us_west_2_jitter))]

    no_vpn_means = [float(Average(raw_lax_jitter)), float(Average(raw_att_lax_jitter)), 
        float(Average(raw_level3_lax_jitter)), float(Average(raw_charter_lax_jitter)), 
            float(Average(raw_comcast_lax_jitter)), float(Average(raw_cox_lax_jitter)), 
                float(Average(raw_gcp_us_west_2_jitter)), float(Average(raw_verizon_lax_jitter)), 
                    float(Average(raw_aws_us_west_1_jitter)), float(Average(raw_alibaba_us_west_1_jitter)), 
                        float(Average(raw_aws_us_west_2_jitter))]


    labels = ['TE', 'ATT', 'Level3', 'Charter', 'Comcast', 'Cox', 'GCP West 2', 'Verizon', 'AWS West 1', 'Alibaba West 1', 'AWS West 2']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, in_vpn_means, width, label='In VPN')
    rects2 = ax.bar(x + width/2, no_vpn_means, width, label='No VPN')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Jitter Averages')
    ax.set_title('Jitter Differences Across All 11 Endpoints')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = int(rect.get_height())
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()














#get_latency_plot_graph()


#get_cloud_latency_plot_graph()

#get_aws_latency_plot_graph()

#get_gcp_latency_plot_graph()

#get_alicloud_latency_plot_graph()

#get_isp_latency_plot_graph()

#get_isp_no_vpn_latency_plot_graph()

#get_isp_with_sigraki_latency_plot_graph()

#get_isp_latency_plot_graph_no_att()

#get_loss_csp_plot_graph()

#get_isp_loss_plot_graph()

#get_in_vpn_isp_loss_plot_graph()

#get_no_vpn_isp_loss_plot_graph()

#get_cloud_jitter_plot_graph()

#get_aws_jitter_plot_graph()

#get_gcp_jitter_plot_graph()

#get_alicloud_jitter_plot_graph()

#get_isp_jitter_plot_graph()

#get_no_vpn_isp_jitter_plot_graph()

#get_with_vpn_isp_jitter_plot_graph()

#get_loss_averages()

get_jitter_averages()
