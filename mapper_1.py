#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)
for row in sys.stdin:

    # splitting the row into a list
    row_data = row.split(',')

    # vin number used for key
    vin_number = row_data[2]

    # building up the value used in key/value pair
    incident_type = row_data[1]
    make = row_data[3]
    year = row_data[5]
    # outlined as described in the handout

    value = (incident_type, make, year)
    print '%s\t%s' % (vin_number, value)

#!/usr/bin/env python
# testing
# $ cat data.csv | python autoinc_mapper1.py | sort
