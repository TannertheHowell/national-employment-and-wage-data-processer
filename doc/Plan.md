# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

* [x] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
* [x] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
* [x] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
* [x] List the algorithms that will be used (but don't write them yet).
* [x] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

* This assignment's overall purpose is to take a large data set, in this case employment data from the Bureau of Labor
Statistics. The data is given in a CSV file that is several million lines long and a few hundred mb. Due to the size of 
the file I will need to cut it down into the appropriate sections/categories in order to make the data usable in a 
reasonable amount of time. The only arguments taken in this assignment will be a directory. 

* The assignment will require the hard coding of the area-titles.csv and 2021.annual.singlefile.csv files into the program.

* Another aspect of this assignment will be the program running at a sufficiently fast pace. 
  * This can be tested using the Performance Benchmark Tool

* The repositories must be set up exactly the same as the sample output. This means each of the directories under data/ 
will have: 
  * README.md
  * area-titles.csv
  * output.txt 
* The output must also have the correct STDOUT output, have deleted all the print()'s for the TODO's while having:
  * no extra newlines
  * no extra spaces
  * no extra quote marks
  * no FIPS codes

* The report must be filled out in the correct way using the rpt dictionary for storage. The use of other programs or
modules is not allowed. These include:
  * os.system()
  * subprocess
  * pipes
  * csv module
  * numpy

* For the FIPS codes:
  * Be careful to deal with overlying areas to exclude them to not double count them
  * The QCEW Area Codes and Titles documentation explains how they are formatted

* Using area-titles.csv
  * It is not to be modified, but to be read in line by line (making me think cat)
  * The str.split can come in handy with help from 'help()' for how to use it
  * FIPS areas that will be included in the report should be stored in a dictionary
  * The report includes not just states but also DC, territories and some other categories like "Out-of-State"
  * The following areas should be excluded to avoid double/triple counting some areas:
    * "U.S. combined" and "TOTAL" FIPS areas
    * "statewide" areas
    * MicroSAs
    * MSAs
    * CSAs
    * Federal Bureau of Investigation – undesignated
  * Helpful tips: 
    * "If your code considers the human-friendly area title, you're doing it wrong"
    * "some FIPS area codes look like integers, always treat them as strings"

* Processing the 2021.annual.singlefile.csv
  * This file should be hard-coded into the program
  * The file has a few key fields:
    * area_fips
    * industry_code
    * own_code
    * total_annual_wages
    * annual_avg_emplvl
    * annual_avg_estabs
  * Handle the file one lien at a time, don't slurp it all like past assignments. 
  * The program should be skipping passed unimportant or duplicate information (using the area_fips field)
  * Strings must be converted to integers, not using eval, just use the int() way. 
  * Handling of All Industries:
    * If the industry_code is 10 and own_code is 0, then the data goes into the all industries portion of the report
  * Handling of Software Publishing Industry:
    * If the industry_code is 5112 and own_code is 5, then add it to the software publishing industry portion of the report

* Lastly, when it comes to speed: get the code working first, then try to make it fast
  * Try to pass through the file only once
  * Avoid nested for loops, two separate ones should do
  * Use a dictionary, not a list or tuples for the FIPS area codes

The overall output of the program should match, to the line and spacing, the sample output in the data/ directory. Each
of them contain an output.txt that I will need to be able to perfectly reproduce. In order to do this I will only be using
the 2021.annual.singlefile.csv to get all the data. I will be using a variety of text tools (cut, paste, etc.) to pull apart
the main file into smaller, more usable directories. The exact layout of that output is in the samples. 

## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [x] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [x] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
*   [x] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

In order to get the smaller dictionaries of data from the single file I will need to do something like the following:
 
open(area-titles.csv)
   for line in file:
      Check the FIPS code based on the area_fips (not area_title)
          if FIPS code is valid:  
              Check that the QCEW Area Code is one of the valid areas
                  if its valid 
                    split the string where appropriate and add it to the dictionary using rpt
                  if not valid, go to the next line
          else:
              skip it (next line by breaking out of this one)
close(area_titles.csv)

* Making sure to exclude the areas like MicroSAs, CSAs and "statewide" areas. Once this is done the output should only
contain the wanted areas. This output should include exactly 3,463 FIPS areas. 
  * Good output should have 3,463 FIPS areas left out of the initial 4,726 areas
  * All the included data like Puerto Rico and the Virgin Islands should be included while the excluded areas like 
     the MSAs and CSAs should all be excluded.

open(2021.annual.singlefile.csv)
    for line in file (go line by line no slurp)
      copyOfLine = line
      if (line.fips == validFips and line.sector == validSector):
          if (industry_code == "10" and own_code == "0"):
             copyOfLine += all industries portion of report
          if (industry_code == "5112" and own_code == "5"):
              copyOfLine += software publishing industry portion of report
      else:
          skip it

close(2021.annual.singlefile.csv)

* This section of the code should output only the valid FIPS codes and industry codes. Good output would only have the 
allowed sections and codes while bad output would include things in the wrong industry, or it could include data that is
not valid for this (like areas that should have been excluded). If the data is exactly right, it should match the output
in the demo files. 

* This is the information that I currently am seeing as needed for this project, though I am sure that this section will
need updating once I get into the next phase. As I find more areas that need functions or other aspects I will come back
and update this section, but for now it is done. 

* [x] Took the quiz and got 10/10

## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [x] More or less working code.
*   [x] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
*   [x] Tag the last commit in this phase `implemented`

This section went actually pretty well. I ended up with a lot more conditional statements that I thought I would have 
used, not a bad thing but there were just more cases to be caught. The overall speed seems fine on the program. I had a 
few issues along the way with having the index be off, but thanks to the numbers being super far off I was able to fix it 
pretty quick. I also had some issues with stripping the "" on my locations, but it worked out fine. Going to commit this 
phase now. 

Part of this phase was running the benchmark tool. While using my computer the big_data.py should finish in under 23.29s.

## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] Tag the last commit in this phase `tested`


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] Tag the last commit in this phase `deployed`
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
