import os

print(os.getenv("password"))

def check_even(number):
    if number % 2 == 0:
        return True
    return False

print(check_even(4))  # Output: True
print(check_even(5))  # Output: False

def cord():
    x= 1
    y=2
    return x ,y

a=cord()
print("cordinates", a)

a3=16
a4=13
a1 = a3/a4
print(a1)
