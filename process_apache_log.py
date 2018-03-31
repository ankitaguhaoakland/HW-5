# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:50:39 2013

@author: mark
"""

import re

def process_apache_log(logfile):
    """
    Count server hits per month from Apache log file.

    Returns dict containing number of server hits by month
    using regex to find the month
    and using a dictionary keyed by month to keep track of running count.


    """

    # local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150

    # Create a compiled regex. Note the I flag for case insensitive matching
    rgx = re.compile(r'(local|remote) - - \[[0-9]{1,2}/([a-zA-Z]{3,3})/',re.I)

    # Initialize counters
    monthly_counts = {}
    monthly_counts['NO_MONTH'] = 0

    # Open the file, read each line, get the month, increment counter
    with open(logfile) as f:
       for line in f:
           # Try to match the regex pattern for this line
           m = re.match(rgx,line)
           if m:
               # We have a match - the month is in the 2nd capture group
               month = m.group(2)
               # Increment the counter dictionary. Use get() to handle case
               # where this month hasn't been seen yet
               monthly_counts[month] = monthly_counts.get(month, 0) + 1
           else:
               # No match
               monthly_counts['NO_MONTH'] = monthly_counts.get('NO_MONTH') + 1

    # All done, print the results
    print (monthly_counts)
    print (sum(monthly_counts.values()))


# The lines below are NOT part of the function above, they are just part of
# this Python script file. They represent a common "pattern" in creating
# Python scripts. Essentially, the if is checking to see if this
# script was run as a 'main' program (either run
# from the command line or run by pushing the Run button in the IDE). If it
# was, it executes the lines after the if statement. If instead,
# this file was imported by another script and then the function called from
# that program, the input and output filenames to process would be passed in as part of the
# function call. Of course, instead of supplying a default filename here,
# we could instead allow for the filename to be passed in as a command line
# argument. See p389 in DWwP for basic info on dealing with command line
# arguments. See the accepted answer in the following StackOverflow question
# for more details: http://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':
    process_apache_log('data/apache.log')
    
