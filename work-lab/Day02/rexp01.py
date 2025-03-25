import re

a = "new job and all is well in the life"

find= r"new job"

match = re.match(find, a)

if match:
    print ("match found", match)
else:
    print ("no match found")