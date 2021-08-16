
#10th of August, 2021
print(ord('G'))
print(ord("b"))

#unicode: inside python world everything is unicode

x='0|hfdiuwe'
type(x)
xp=u'0|@WIKEFJ' # regular string # to represent byte string b''
type(xp)
# We can see both are unicode
while True:
    data=mysock.recv(512)
    if(len(data))<1:
        break
    print(data.decode())
mysock.close()   # Here I have to define mysock

x=-1
if x<2:
    print('Below 2')
elif x<0:
    print('Negative')
else:
    print('Something Else')

zap="hello there bob"
print(zap[4])


def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()

def hello():
    print("Hello")
    print("There")
x=10
x=x+1

# Very interesting

first='Test '
second=4
print(first * second)

inp=input('What is your name?\n')
print(inp)

# 11th of August, 2021
n=input()
m=input()
if n==m:
    print('n is equal to m')
else:
    if n>m:
        print('n is greater than m')
    else:
        print('n is less than m')
print('Done!')

# Degree F to C
inp=input('Enter a Ferhenite value:')
f=float(inp)
cel=(5*f/9)-32*5/9
print(cel)

# Using the try and except block
inp=input('Enter a Ferhenite value:')
try:
    f=float(inp)
    cel=(5*f/9)-32*5/9
    print(cel)
except:
    print('Run again and Enter a valid number:')

Hourly Rate:
inp1=input('Enter hour')
inp2=input('Enter hourly rate')
h=float(inp1)
r=float(inp2)
if h<=40:
    pay=h*r
    print(pay)
elif h>40:
    pay=((h-40)*r*1.5)+40*r
    print(pay)
print('Done!')

#13th of August, 2021
# Math function: before using math function, we need to import it first, for example, import math

import math
degree=45
radians=degree/360*2*math.pi
p=math.sin(radians)
print(p)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def print_twice(bruce): # An indentation will be required after def a function// here in print_twice, we call everybody bruce.
    print(bruce)
    print(bruce)
# Defining function is a very interesting thing in python
# This is very important to remember that something.(dot) means importing something
print_twice(math.pi)
golden = (math.sqrt(5) + 1) / 2

# To return a result from a function, we use the return statement in our function.
# For example, we could make a very simple function called add two that adds two
# numbers together and returns a result.

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)

#module object: A value created by an import statement that provides access to
#the data and code defined in a module

def coputepay(h,r):
    multply=h*r
    return multply
x= coputepay(5,15)
print(x)

#Loop
n=10
while n>5:
    print(n)
    n=n-1 # this is called iteration variable and it means loop is changing, if we don't use it, then it means this loop will continue for the forever
print('Done!')

n=10
while n>5:
    print('l')
    print(n)
    n=n+1 # this is called iteration variable and it means loop is changing, if we don't use it, then it means this loop will continue for the forever
print('Done!')
# Do not run it /it will run for the forever
n=10
while True:
    print(n, end='')
    n=n-1 # this is called iteration variable and it means loop is changing, if we don't use it, then it means this loop will continue for the forever
print('Done!')

