

# Count number of accident occurrences for the vehicle make and year
# Follow the previous mapper template to create a mapper that reads the previous reducer output.
# The value should be the count of 1.


#!/usr/bin/python
import sys


#loading data using stdin - reading from reducer1
for row in sys.stdin:

    # splitting the row into a list
    row_data = row.split('\t')

    # building up the key used in key/value pair
    value = (row_data[1])
    make = value[1]
    year = value[2]
    composite_key = make + year # The output key should be the composite key made up of the concatenation of vehicle make and year.
    print '%s\t%s' % (composite_key, 1)

# testing
# $ cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort
