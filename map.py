

import re
import sys

for line in sys.stdin:
    val = line.strip()
    valsplit = val.split(', ')
    country = valsplit[2]
    cost = float(valsplit[4])
    print "%s\t%s" % (country, cost)
