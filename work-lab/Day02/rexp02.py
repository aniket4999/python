import re

text= "i will be successful"
ser= r"i will be successful"

search = re.search(ser,text)

if search:
    print("found", search)
else:
    print("not found")