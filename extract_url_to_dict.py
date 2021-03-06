# extract_url_to_dict.py
# This program will store the URLs as a Dictionary 
# object in the list with the resource and parameter 
# names and values separated out eg
#
# Author: Tomasz

import re
import pprint

filename = "access.log"  # file we want to analyze

with open(filename, 'r') as access_logs:
    # loop through each line and extract
    for line in access_logs:
        rsc = re.split ('\/', (re.split ( '\?', line)[0]))[3]   # resource
        act = re.split('&',(re.split ('=', line)[1]))[0]        # action
        item = re.split('&',(re.split ('=', line)[2]))[0]       # item
        product = re.split('&',(re.split ('=', line)[3]))[0]    # product
        session = re.split(' ',(re.split ('=', line)[4]))[0]    # session
        
        # create a new dictionary and fill in extracted information
        para_dict = {'resource': rsc, 
                    'parameters': {'action': act , 'itemId': item ,'productId' : product, 'JSESSIONID' : session
        }
        }

# print dictionary out
pprint.pprint(para_dict, sort_dicts=False)
