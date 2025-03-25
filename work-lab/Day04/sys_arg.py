import sys

def add(a,b):
    r1= a + b
    return(r1)

def mul(a,b):
    r2=a*b
    return(r2)

a= float(sys.argv[1])
operator = sys.argv[2]
b= float(sys.argv[3])

if operator == "add":
    output = add(a,b)
    print(output)
