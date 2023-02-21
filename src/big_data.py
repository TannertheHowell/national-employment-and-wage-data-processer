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
    splitLine = line.split(",")
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
        acceptedAreas[splitLine[0]] = splitLine
f.close()

print("TODO: if opening the file 'sys.argv[1]/2021.annual.singlefile.csv' fails, let your program crash here")  # DELETE ME
f = open(sys.argv[1]+"/2021.annual.singlefile.csv")

print("TODO: Collect information from 'sys.argv[1]/2021.annual.singlefile.csv'")  # DELETE ME  	  	  

print("TODO: Fill in the report dictionary for all industries")  # DELETE ME  	  	  
rpt['all']['num_areas']           = 1337  	  	  

rpt['all']['total_annual_wages']  = 13333337  	  	  
rpt['all']['max_annual_wage']     = ["Trantor", 123456]  	  	  

rpt['all']['total_estab']         = 42  	  	  
rpt['all']['max_estab']           = ["Terminus", 12]  	  	  

rpt['all']['total_empl']          = 987654  	  	  
rpt['all']['max_empl']            = ["Anacreon", 654]  	  	  


print("TODO: Fill in the report dictionary for the software publishing industry")  # DELETE ME  	  	  
rpt['soft']['num_areas']          = 1010  	  	  

rpt['soft']['total_annual_wages'] = 101001110111  	  	  
rpt['soft']['max_annual_wage']    = ["Helicon", 110010001]  	  	  

rpt['soft']['total_estab']        = 1110111  	  	  
rpt['soft']['max_estab']          = ["Solaria", 11000]  	  	  

rpt['soft']['total_empl']         = 100010011  	  	  
rpt['soft']['max_empl']           = ["Gaia", 10110010]  	  	  


after = time.time()  	  	  
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	  	  


# Print the completed report  	  	  
print_report(rpt)  	  	  

print("\n\nTODO: did you delete all of the TODO messages?")  # DELETE ME  	  	  
