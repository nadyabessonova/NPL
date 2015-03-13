import sys

(last_key, sum) = (None, 0)
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    try:
        val = float(val)
    except ValueError:
        continue
    
    if last_key == key:
        sum = sum + val
    else:
        if last_key:
        
            print "%s\t%s" % (last_key, sum)
        (last_key, sum) = (key, val)

if last_key == key:
    print "%s\t%s" % (last_key, sum)


