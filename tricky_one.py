# tricky_one.py
# 
# Read the access.log into a dataframe (see lab)
# Set the date time to be the index (you will need to manipulate this data, see lab)
# Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
# Use groupBy to get the sum of all the data downloaded by each sessionId.
# Create a plot of this (type of your choice)
#
# author: Tomasz

import pandas as pd
import re
import matplotlib.pyplot as plt

path = './data/'
logFilename = path + 'sm_access.log'
colNames = ('ip','dash','user','time','request','status code',
            'size of response','referer','user agent','dunno')

#read data
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

# Removing '[' and ']'
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
# Formatting data time
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
# Dropping columns with dashes only
df.drop(columns=['dash', 'user'], inplace=True)

# index to the date column
df = df.set_index(['time'])

# regex to extract session id
def extractor (line):
    reg = re.search('(JSESSIONID=\S+)', line).group()
    session_id = re.split('=', reg)[1]
    return session_id

df['session'] = df['request'].apply(extractor)

# get the sum of all the data downloaded by each sessionId.
print(df.groupby(by=['session'])['size of response'].sum())

# Create a plot of this (type of your choice)
plt.figure(figsize=(7, 7))

plotdata = df.groupby(by=['session'])[['size of response']].sum()
plotdata['size of response'].plot(kind='bar')

# Set the plot labels
plt.title("Data downloaded by SessionID")

# Show the graph
plt.show()







