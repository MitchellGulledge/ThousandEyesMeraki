import csv
import pandas as pd
# importing mean() 
from statistics import mean 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# defining function to calculate mean of a list
def Average(lst): 
    return mean(lst)

# openening CSV file that contains all tests and converting to pandas df
df_raw_test_csv = pd.read_csv('ThousandEyesTest.csv', index_col=0)


# set of lists for latency for each test
cogent_ny1_latency = []
cogent_ny2_latency = []
comcast_ny_latency = []
charter_ny_latency = []
level3_ny_latency = []
aws_east_1_latency = []
aws_east_2_latency = []

# set of lists for loss for each test
cogent_ny1_loss = []
cogent_ny2_loss = []
comcast_ny_loss = []
charter_ny_loss = []
level3_ny_loss = []
aws_east_1_loss = []
aws_east_2_loss = []

# set of lists for jitter for each test
cogent_ny1_jitter = []
cogent_ny2_jitter = []
comcast_ny_jitter = []
charter_ny_jitter = []
level3_ny_jitter = []
aws_east_1_jitter = []
aws_east_2_jitter = []

# creating list so that we can have X axis for histogram
test_avg_name_list = ["Cogent 1", "Cogent 2", "Charter", "Level3", "Comcast", "AWS_US_East_1",\
     "AWS_US_East_2"]

# iterating through df_raw_test_csv to build the three sublists for the three separate graphs
for index, row in df_raw_test_csv.iterrows():

    # if statement that matches test name and appends metrics (latency/loss/jitter) to appropriate list
    if "Ashburn, VA (AWS us-east-1)" in str(row['test_name']):

        aws_east_1_latency.append(row['test_latency'])
        aws_east_1_loss.append(row['test_loss'])
        aws_east_1_jitter.append(row['test_jitter'])

    elif "Columbus, OH (AWS us-east-2)" in str(row['test_name']):

        aws_east_2_latency.append(row['test_latency'])
        aws_east_2_loss.append(row['test_loss'])
        aws_east_2_jitter.append(row['test_jitter'])

    elif "New York, NY (CenturyLink)" in str(row['test_name']):
        level3_ny_latency.append(row['test_latency'])
        level3_ny_loss.append(row['test_loss'])
        level3_ny_jitter.append(row['test_jitter'])

    elif "New York, NY (Charter)" in str(row['test_name']):
        charter_ny_latency.append(row['test_latency'])
        charter_ny_loss.append(row['test_loss'])
        charter_ny_jitter.append(row['test_jitter'])

    elif "New York, NY (Cogent)" in str(row['test_name']):
        cogent_ny1_latency.append(row['test_latency'])
        cogent_ny1_loss.append(row['test_loss'])
        cogent_ny1_jitter.append(row['test_jitter'])

    elif "New York, NY 2 (Cogent)" in str(row['test_name']):
        cogent_ny2_latency.append(row['test_latency'])
        cogent_ny2_loss.append(row['test_loss'])
        cogent_ny2_jitter.append(row['test_jitter'])

    elif "New York, NY (Comcast)" in str(row['test_name']):
        comcast_ny_latency.append(row['test_latency'])
        comcast_ny_loss.append(row['test_loss'])
        comcast_ny_jitter.append(row['test_jitter'])


print("Cogent NY 1 Average Latency is: " + str(Average(cogent_ny1_latency)))
print("Cogent NY 2 Average Latency is: " + str(Average(cogent_ny2_latency)))
print("Comcast NY Average Latency is: " + str(Average(comcast_ny_latency)))
print("Level3 NY Average Latency is: " + str(Average(level3_ny_latency)))
print("Charter NY Average Latency is: " + str(Average(charter_ny_latency)))
print("AWS US East 2 Average Latency is: " + str(Average(aws_east_2_latency)))
print("AWS US East 1 Average Latency is: " + str(Average(aws_east_1_latency)))

print("Cogent NY 1 Average Loss is: " + str(Average(cogent_ny1_loss)))
print("Cogent NY 2 Average Loss is: " + str(Average(cogent_ny2_loss)))
print("Comcast NY Average Loss is: " + str(Average(comcast_ny_loss)))
print("Level3 NY Average Loss is: " + str(Average(level3_ny_loss)))
print("Charter NY Average Loss is: " + str(Average(charter_ny_loss)))
print("AWS US East 2 Average Loss is: " + str(Average(aws_east_2_loss)))
print("AWS US East 1 Average Loss is: " + str(Average(aws_east_1_loss)))

print("Cogent NY 1 Average Jitter is: " + str(Average(cogent_ny1_jitter)))
print("Cogent NY 2 Average Jitter is: " + str(Average(cogent_ny2_jitter)))
print("Comcast NY Average Jitter is: " + str(Average(comcast_ny_jitter)))
print("Level3 NY Average Jitter is: " + str(Average(level3_ny_jitter)))
print("Charter NY Average Jitter is: " + str(Average(charter_ny_jitter)))
print("AWS US East 2 Average Jitter is: " + str(Average(aws_east_2_jitter)))
print("AWS US East 1 Average Jitter is: " + str(Average(aws_east_1_jitter)))




latency_performance_list = [float(Average(cogent_ny1_latency)), float(Average(cogent_ny2_latency)), \
    float(Average(charter_ny_latency)), float(Average(level3_ny_latency)), \
        float(Average(comcast_ny_latency)), float(Average(aws_east_1_latency)), \
            float(Average(aws_east_2_latency))]

loss_performance_list = [float(Average(cogent_ny1_loss)), float(Average(cogent_ny2_loss)), \
    float(Average(charter_ny_loss)), float(Average(level3_ny_loss)), \
        float(Average(comcast_ny_loss)), float(Average(aws_east_1_loss)), \
            float(Average(aws_east_2_loss))]

jitter_performance_list = [float(Average(cogent_ny1_jitter)), float(Average(cogent_ny2_jitter)), \
    float(Average(charter_ny_jitter)), float(Average(level3_ny_jitter)), \
        float(Average(comcast_ny_jitter)), float(Average(aws_east_1_jitter)), \
            float(Average(aws_east_2_jitter))]

######### Below section of code that is commented out grabs average latency across all tests

# x-coordinates of left sides of bars  
#left = [1, 2, 3, 4, 5, 6, 7] 
  
# heights of bars 
#height = latency_performance_list
#height = [1, 2, 3, 4, 5, 6, 7]
  
# labels for bars 
#tick_label = test_avg_name_list 
  
# plotting a bar chart 
#plt.bar(left, height, tick_label = tick_label, 
        #width = 0.8, color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan']) 
  
# naming the x-axis 
#plt.xlabel('ISP / CSP') 
# naming the y-axis 
#plt.ylabel('Latency Average') 
# plot title 
#plt.title('Average Latency Across All Tests') 
  
# function to show the plot 
#plt.show() 


####### the code below section calculates average loss across all tests

# x-coordinates of left sides of bars  
#left = [1, 2, 3, 4, 5, 6, 7] 
  
# heights of bars 
#height = loss_performance_list
#height = [1, 2, 3, 4, 5, 6, 7]
  
# labels for bars 
#tick_label = test_avg_name_list 
  
# plotting a bar chart 
#plt.bar(left, height, tick_label = tick_label, 
#        width = 0.8, color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan']) 
  
# naming the x-axis 
#plt.xlabel('ISP / CSP') 
# naming the y-axis 
#plt.ylabel('Packet Loss Average') 
# plot title 
#plt.title('Average Loss Across All Tests') 
  
# function to show the plot 
#plt.show() 

####### the code below section calculates average jitter across all tests

# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5, 6, 7] 
  
# heights of bars 
height = jitter_performance_list
#height = [1, 2, 3, 4, 5, 6, 7]
  
# labels for bars 
tick_label = test_avg_name_list 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan']) 
  
# naming the x-axis 
plt.xlabel('ISP / CSP') 
# naming the y-axis 
plt.ylabel('Jitter Average') 
# plot title 
plt.title('Average Jitter Across All Tests') 
  
# function to show the plot 
plt.show() 
