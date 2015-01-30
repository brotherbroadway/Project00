__author__ = 'JTR'

# Python Tutorial 3.2 - 4 https://docs.python.org/3/tutorial/index.html

# 'while' Statements

a, b = 0, 1

while b < 10:
    print(b)
    a, b = b, a+b

i = 256*256
print("The value of i is", i)

# 4. More Control Flow Tools

x = int(input("Please enter an integer: "));
if x < 0:
    x = 0
    print("Negative changed to zero")
    elif x == 0:
    print("Zero")
    elif x == 1:
    print("Single")
    else:
    print("More")

# why isnt this elif working