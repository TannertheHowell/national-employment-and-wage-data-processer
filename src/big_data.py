#!/usr/bin/env python  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

import time  	  	  
import sys  	  	  
from report import print_report  	  	  


# print_report takes a dictionary with these contents:  	  	  
rpt = {  	  	  
        'year': 2021,  	  	  

        'all': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  

        'soft': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  
}  	  	  

# Open the file, if it crashes it'll output the error
if len(sys.argv) < 2:
    print("Usage: src/big_data.py DATA_DIRECTORY")
    sys.exit(1)

print("Reading the databases...", file=sys.stderr)  	  	  
before = time.time()  	  	  

f = open(sys.argv[1]+"/area-titles.csv")

# Empty dictionary to store the correct FIPs areas
acceptedAreas = {}

for line in f:
    splitLine = line.split(",", 1)
    # Excluding areas to avoid double/triple counting
    if splitLine[0].startswith('"US'):
        continue
    elif splitLine[0].startswith('"C'):
        continue
    elif splitLine[0].startswith('"M'):
        continue
    elif splitLine[0].startswith('"C'):
        continue
    elif splitLine[0].startswith('"a'):
        continue
    elif splitLine[0].endswith('000"'):
        continue
    else:
        acceptedAreas[splitLine[0]] = splitLine[1].rstrip()[1:-1]
f.close()

f = open(sys.argv[1]+"/2021.annual.singlefile.csv")

for line in f:
    separatedLine = line.split(",")
    if separatedLine[0].startswith('"area_fips"'):
        continue
    if separatedLine[0] not in acceptedAreas:
        continue

    if separatedLine[2] == '"10"' and separatedLine[1] == '"0"':
        # add it to the all industries report
        rpt['all']['num_areas'] += 1

        rpt['all']['total_annual_wages'] += int(separatedLine[10])
        if int(separatedLine[10]) > rpt['all']['max_annual_wage'][1]:
            rpt['all']['max_annual_wage'] = [acceptedAreas[separatedLine[0]], int(separatedLine[10])]

        rpt['all']['total_estab'] += int(separatedLine[8])

        if int(separatedLine[8]) > rpt['all']['max_estab'][1]:
            rpt['all']['max_estab'] = [acceptedAreas[separatedLine[0]], int(separatedLine[8])]

        rpt['all']['total_empl'] += int(separatedLine[9])

        if int(separatedLine[9]) > rpt['all']['max_empl'][1]:
            rpt['all']['max_empl'] = [acceptedAreas[separatedLine[0]], int(separatedLine[9])]

    if separatedLine[2] == '"5112"' and separatedLine[1] == '"5"':
        # add it to the software publishing industry report
        rpt['soft']['num_areas'] += 1

        rpt['soft']['total_annual_wages'] += int(separatedLine[10])
        if int(separatedLine[10]) > rpt['soft']['max_annual_wage'][1]:
            rpt['soft']['max_annual_wage'] = [acceptedAreas[separatedLine[0]], int(separatedLine[10])]

        rpt['soft']['total_estab'] += int(separatedLine[8])

        if int(separatedLine[8]) > rpt['soft']['max_estab'][1]:
            rpt['soft']['max_estab'] = [acceptedAreas[separatedLine[0]], int(separatedLine[8])]

        rpt['soft']['total_empl'] += int(separatedLine[9])

        if int(separatedLine[9]) > rpt['soft']['max_empl'][1]:
            rpt['soft']['max_empl'] = [acceptedAreas[separatedLine[0]], int(separatedLine[9])]

after = time.time()  	  	  
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	  	  

# Print the completed report  	  	  
print_report(rpt)  	  	  

