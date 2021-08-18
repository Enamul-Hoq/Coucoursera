#10th of August, 2021
import os

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

#16th of August-2021
import sys
print(sys.maxsize)
type(sys.maxsize)
i='ABC'
print(i*3)

while True:
    line=input('>') # Important to remember that = is an assignment operator
    print("B")
    if line[0]=='#':
        continue
        print('A')
    if line=='done':
        break
    print(line)
print('Done!')

# More about while loop

i=1
while i<=10:
    print('Shimul',i)
    i=i+1

kl="amamdfhewgrtuwei"
kl.endswith(i)
x=input(int())
while x>0:
    print('pl is positive')
    x=x-1
print('Done') # These codes don't work because > not supported between instances of 'str' and 'int'

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

i=1
while i<6:
    print(i)
    if i==2:
        i+=1
        continue
    if i==5:
        break
    i+=1
i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

# 17th 0f August 2021

f=int(input('Enter a number:'))
while f<10:
    if f==3:
        continue
    print(f)
    f+=1
print('Done!')

import random
n=random.randrange(20,80,10)
#print(n)
while n<=80:
    n+=1
    if n>60:
        print('Your guessing number is too high.')
    if n<50:
        print('Your guessing number is too low.')
    else:
        print('Congrats! Your guess is correct')
print('Done!')

#select random number between 1 to 10
#user has to guess it within five attempts
#Hints 1) number is too high
      #2) number is too low
#when the number matches it will print that you are done! congrats with attempts


import random
numbers=random.randint(1,10)
number_of_attempts=0
player_name=input('Hello! May I have your name, please?:')
print('Alright then!Mr.'+ player_name + ' I am guessing a number between 1 to 10. Are you playing? Go ahead')
while number_of_attempts<5:
    number_of_attempts+=1
    guess_number=int(input())
    if guess_number>numbers:
        print("Your number is too high" )
    if guess_number<numbers:
        print("Your number is too low ")
    if guess_number==numbers:
        break
if guess_number==numbers:
    print('Congrats! You guessed correct number in ' + str(number_of_attempts) +' tries')
else:
    print('Sorry! You failed to choose correct number in '+ str(number_of_attempts)+
    ' tries')

while True:
    line = input('> ')
    if line == 'done':
        break
    #print(line)
print('Done!')

# For Loop
total=0
for x in [3,7,9,2,1,5]:
    total=total+x
    print('Total:',total)


total=0
for x in [3,7,9,2,1,5]:
    total=total+x
print('Total:', total)

# Finding the largest value or lowest value inside the list

largest=None
for n in [3,7,9,2,1,5]:
    if largest is None or n > largest:
        largest=n
    print('Loop :',n, largest)
print("Largest:",largest)

p=[3,7,9,2,1,5]
maxvalue=p[0]
print(min(p))
print(max(p))

# String Strings are an example of Python objects
index=0
fruit='bannana'
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index+=1
print('Done!')

word='banna'
count=0
for letter in word:
    if letter=='a':
        count+=1
print(count)


word.find('a') # to search position of a string

# to open the file mbox.txt, which should be stored in the same
#folder that you are in when you start Python
fhand = open('mbox.txt')
print(fhand)

import os
fop=os.system('pythonlearn.pdf')
inp=fop.read()
print(len(fop))

