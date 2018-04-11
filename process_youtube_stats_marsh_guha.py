# -*- coding: utf-8 -*-
"""
Created on 2018-03-20

@author: misken
"""

import re


def process_youtube(fn_youtube , fn_out, cat_id):
    """
    Function
    --------
    process_youtube

    Use regex to create a file with records only from a specific category_id.

    Parameters
    ----------
    fn_youtube : str
        Name of YouTube trending stats file

    fn_out : str
        Name of new YouTube trending stats file containing only records of
        interest.

    cat_id : str
        Category ID number to match, input as a string

    Returns
    -------
    Nothing. Counts of lines matched and not matched are displayed
    at the end. For lines in category_id 28, the counts by date are captured
    in a dictionary and displayed at the end.

    Example
    -------
    process_youtube('USvideos.csv' , 'USvideos_SciTech.csv', '28')

    """

    # Initialize empty dict for counts by date
    daily_counts = {}

    #Turns the input into a string
    cat_id = format(cat_id)

    # regex for line filter - only include lines from category_id = 28
    # Snippet from first line:
    # 2kyS6SvSYSE	17.14.11	WE WANT TO TALK ABOUT OUR MARRIAGE	CaseyNeistat

    re_filter = re.compile(r'\w+,\s?([0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}),\s?\"(.+?)\",\s?\"(.+?)\",\s?' + cat_id, re.I)

    # Initialize counters
    num_lines_matched = 0
    num_lines_not_matched = 0

    # Initialize list to store output lines
    outputlines = []

    # Open the input file
    with open(fn_youtube) as yt:

        # Loop over the lines in the file
        for line in yt:
            # Let's strip off any end of line characters
            line = line.strip('\n')

            # See if regex for filtering matches this line
            mfilter = re.match(re_filter,line)

            # If we matched, update counters and store line in list for output
            if mfilter:

                # Increment counter of number of lines matched
                num_lines_matched += 1

                # Get the date from first capture group
                trending_date = mfilter.group(1)

                # Increment count by trending date
                daily_counts[trending_date] = daily_counts.get(trending_date, 0) + 1

                # Append line to master output list
                outputlines.append(line)

            else:
                # Increment number of lines not matched counter
                num_lines_not_matched += 1


    # Write the output file
        # There are a few ways to write out a list of strings to a file. Figure
        # out one way to do it and then do it.
    thefile = open(fn_out,'w')
    for item in outputlines:
        thefile.write("%s\n" % item)

    # # Print out the counts dictionary
    for x in daily_counts.keys():
        print ("%s:\t%s videos\n" % (x, daily_counts[x]))

    # All done, print the results
    print("\nNum lines matched --> {}".format(num_lines_matched))
    print("\nNum lines not matched --> {}".format(num_lines_not_matched))


if __name__ == '__main__':
    process_youtube('./data/USvideos_no_desc.csv', 'USvideos_SciTech.csv',28)