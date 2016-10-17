'''
Finds log occurences per hour
'''

import re

my_dict = {}

for line in open("input001.txt", "r"):
	matchObj = re.search(r'\d{4}:\d{2}:\d{2}:\d{2}', line)
	if matchObj and '1.1" 200' in line:
		if (matchObj.group()[5:7]) in my_dict:
			my_dict[matchObj.group()[5:7]] += 1
		else:
			my_dict[matchObj.group()[5:7]] = 1
print (my_dict)