# extract_url.py
# This program will extract the URLs from an access.log file.
#
# Author: Tomasz

import re

filename = "access.log"  # file we want to analyze

#open file and check each line against the regex
with open(filename, 'r') as access_logs:
    for line in access_logs:
        regex = "/[^0-9A-Z/][^w][[a-zA-Z.?=0-9-&/]{1,}"
        x = re.findall(regex, line)  # find matches
        print(x) #print out results