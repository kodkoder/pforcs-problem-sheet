# collatz.py
# This program will extract the URLs from an access.log file.
#
# Author: Tomasz

import re

filename = "access.log"

with open(filename, 'r') as access_logs:
    count = 0
    for line in access_logs:
        regex = "/[^0-9A-Z/][^w][[a-zA-Z.?=0-9-&/]{1,}"
        x = re.findall(regex, line)
        print(x)