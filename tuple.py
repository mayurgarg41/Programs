'''atup = ( 1,2,'unix')
print (atup)
"""atup = 5"""
print (atup)

btup = atup
print (btup)'''

'''
#dic = {key:value, key:value}
addict = {"chap1":10, 20:"chap2", "chap3":30}
print (addict)
print (addict["chap1"])
print (addict[20])



name = 'I love python programming'
'''

'''
print(name.capitalize())
print (name.count('p'))
print (name.split(' '))
clist = name.split(' ')
print (clist[1])

name1 = "   lets see  "
print (name1)
name2 = name1.lstrip()
print (name2)

# replace p with perl
print (name.replace('p', 'perl'))'''


'''
alist = [1,'e',5]
print (alist)
alist.reverse()
print (alist)
alist.insert(0,3)
print (alist)
'''


'''
dlist = [1,2,4]
print (dlist)
dlist.append('unix')
print(dlist)

dlist.append([2,5])
print(dlist)
print(dlist.count(2))

dlist.extend([6,7,8])
print(dlist)


removed = dlist.pop(3)
print(removed)
print(dlist)
dlist.reverse()
print(dlist)
dlist.pop(3)
dlist.sort()
print(dlist)
'''

'''
#set in python
aset = {1,2,3,3,4}
bset = {2,4}
print(aset, bset)
print("Union of two sets",aset.union(bset))

print("Intersection of two sets",aset.intersection(bset))

print(bset.issubset(aset))
'''

#write a program to capture any filename from keyboard and display  its filename and extension separately.
''' Output:
Enter any filename :

filename:
extension: '''

'''
astring = input()
print(astring)
alist = astring.split('.')
print("filename: ",alist[0])
print("extension: ",alist[1])
'''


#write a program to capture two numbers separately from keyboards and display sum
''' Enter 1st number :
enter 2nd num;
sum of the numbers:
'''
'''
a = input("Enter 1st number")
c = int(a)
b = input ("Enter 2nd number")
d = int(b)
print ("sum of numbers", c+d)
'''
#write program to display al duplicates of list alist = [10, 20, 30, 10, 35, 20, 67, 89, 20, 10]
'''Output to display all unique numbers.'''

'''
alist = [10, 20, 30, 10, 35, 20, 67, 89, 20, 10]

blist = set(alist)
print( 'Output to display all unique numbers.', blist)
blist = list(blist)
'''

#write program to capture the string "Python is general purpose interpreted cross platform programming lang" from the kepboard
# and eprfom below operations.
'''
1. display the string in upper case.
2. count of no. of occurences of p in the string and display it
3. replace python to ruby in string.
4. count the number of words in string  len(str.split(" "))
5. count the number of characters and display.   len(str)
6. remove spaces if have any
'''

#bstring = input ("Input the string:")

'''
astring = "Python is general purpose interpreted cross platform programming lang"

print("string in upper case:", astring.upper())

print("no. of occurences of p in the string: ", astring.count('p'))

print("new string: ", astring.replace("Python", "ruby"))

print ("number of words:" , len(astring.split(' ')))

print ("number of characters:" , len(astring))

print ("Removed spaces from both : ", astring.strip())
'''

# define empty list in your program and perform operations
'''
append 10 to list
append 20
append 50
extend the list with 90,20,40,32, 50, 65, 98, 907
remove all duplictaes from the list
remove 50 from the list
sort all elements in descending order
convert list to tuple and display
'''
'''
alist = []
print(" Empty list:", alist, type(alist))
alist.append(10)    
alist.append(20)
alist.append(50)
alist.extend([90,20,40,32, 50, 65, 98, 907])
print(alist)

bset = set(alist)
print (bset)

alist.remove(50)
print("remove first 50", alist)

alist.sort(reverse=True)
print( "descend sort", alist)

atuple = tuple(alist)
print(atuple)

#print(set(alist))

'''
# inundation
'''
first = 10
second = 20
if first > second :
    print (first, " is largest")
else: print (second, " is largest")
'''
'''
# range only works with list and tuple

print(tuple(range(1,10)))
print(list(range(1,10)))

#display numbers in step 2 order
print(list(range(1,10,2)))

#display number in reverse order
print(list(range(10,-10,-2)))
'''
#increment and decrement operators like C are not allowed in python.
'''
#for loop with list
alist = (10,2,'unix')
for val in alist:
    print (val)
print ('end of list')

#for loop with range
for val in range(1,5):
    print(val)

#display all the keys
adict = {'chap1':10, 'chap2':20}
for val in adict.keys():
    print(val)
    print(adict[val])


#for loop with string
name ='python program'
for char in name:
    print(char)

#for loop with set
aset = {2,2,3,3}
for val in aset:
    print(val)
'''


#write program to capture string from keyboard.
'''
string is too short if length is < 5
string is too long if length is > 30
'''

'''
astring = input('Enter the string:')
if len(astring) < 5:
    print ('string is too short')
elif len(astring) > 10:
    print ('string is too long')
else:
    print('string is appropriate')
'''


#convert the string into lowercase if string is uppercase
#convert the string into uppercase if string is lowercase
'''
astring = input('Enter the string:')
if astring.isupper():
    print('String is converted to lower',astring.lower())
elif astring.islower():
    print('String is converted to upper',astring.upper())
else: print(" The original string is ", astring)
'''

#define list as below and display all unique elements of list and length of list.
'''
alist = ['google.com', 'unix.com', 'facebook.com','google.com','linkedin.com']
output: [10,8,12,12]
'''
'''
alist = ['google.com', 'unix.com', 'facebook.com','google.com','linkedin.com']
aset = set(alist)
print (aset)
alist = list(aset)
print(len(alist))
output = []
for val in range(0, len(alist)):
    #output.append(len
    output.append(len(alist[val]))
print(output)
'''

#write program to capture the input as below and convert into list
'''
String - unix,java,oracle,hadoop
output: ['unix','java','oracle','hadoop']
'''

'''
astring = input('Enter the string:')
print(astring)
alist = astring.split(',')
print(alist)

'''

#write program to display all odd numbers from 500 to 400

'''
for val in range(499,400,-2):
    print (val)
'''

#write program to display below output
'''
1.py
2.py
.
.
.
11.py'''

'''
for i in range(1,12):
    b = str(i)+'.py'
    print(b)
'''

#repetition
'''
print('python' * 3)
'''

#Write a program to accept a string and reverse the string.
#Enter string: python
#Rverse: nohtyp

'''
astring = input('Enter a string: ')
alist = list(astring)
alist.reverse()
print(alist)

bstring = ''.join(alist)
print(bstring)
'''

#method 2
'''
name = "python"
print(name[0:3])
print(name[::-1])
'''


#Write program that accepts string and calculate number of digits and letters
'''
Enter any string: py3thon
No. of alphabets: 5
No. of digits : 1
'''

'''
astring = input('Input the string:')
digit = 0
alpha = 0
for item in list(astring):
    if item.isalpha():
        alpha +=1
    elif item.isdigit():
        digit +=1

print('alpha', alpha, 'digit', digit)
'''

# Write program to accept string and calculate teh number of upper case letters and lower case letters.

'''
astring = input('Input the string:')
upper = 0
lower = 0
for item in list(astring):
    if item.isupper():
        upper +=1
    elif item.islower():
        lower +=1   
print(upper, lower)
'''

#Write program to accept month from keyboard and display the season
''' Jan to Mar -> Winter
Apr to Jun -> Summer
July to Oct -> rainy'''

'''
month = input('Enter the first 3 char of month:' )
Mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
g=0
i=99
for item in Mon:
    if item == month:
        i=g
    g+=1

print(i)
if i>=0 and i<4:
    print('Winter')
elif i>=4 and i<7:
    print('Summer')
elif i>=7 and i<11:
    print('Rainy')
else: print('Invalid Month')
 '''
 #alternate method
 
'''
month = input('Enter the first 3 char of month:' )
if month in ['Jan','Feb','Mar']:
    print('Winter')
if month in ['Apr','May','Jun']:
    print('Summer')
'''
        

#Write program to check validity of password input by user
'''
Criteria-
1. Atleast 1 character from [$#@]
2. Min length :6
3. Max length :12
display valid password if all condiions are met else invalid password
'''

'''
passwd = input('Enter password:')
Valid = 0
if len(passwd)<6 or len(passwd)>12:
    print('Invalid password')
else:
    for i in passwd:
        if i in ['@','#','$']:
            Valid =1

if Valid == 1:
    print('Valid password')
else:
    print('Invalid password')    
'''

#alternate method

'''
passwd = input('Enter password:')
Valid = 0
if len(passwd)>=6 and len(passwd)<=12 and ('#' in passwd or '$' in passwd or '#' in passwd):
    valid =1
    
if valid == 1:
    print('Valid password')
else:
    print('Invalid password') 
'''


#Library functions

'''
import math
print(math.acos(0.3))

import math as m
print (m.tan(2))
'''

#write program to list all files and directories in current path
'''
import os
print(os.listdir('C:/'))

for val in os.listdir('C:/'):
    if os.path.isfile('C:/'+ val):
        print(val)

'''
#Write a program to print and delete all files ending in .pyt from current directory
'''
import os
for file in os.listdir():
    if file.endswith('.py'):
        print(file)

'''

#executing system commands in python
#alternate way is os.system
'''
import subprocess
print(subprocess.getoutput('dir'))
'''

#write program to create 100 directories in below format. dir1, dir2

'''
import os
path = os.getcwd()
print(path)
for val in range(1,10):
    dirname = path + '\dir' + str(val)
    print(dirname)
    os.mkdir(dirname)
#print(os.path.join(path,'A')
'''

#write program to display all files and directories in below format
""" Files
-----
file 1
file 2

Directories
----------   
dir 1
dir 2 
"""
'''
import os

files = []
dirs = []

for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
    elif os.path.isdir(file):
        dirs.append(file)

print('files')
print('-------------')
for file in files:
    print (file)

print('dirs')
print('-------------')
for file in dirs:
    print (file)
'''

#write a program to create a folder 'backup' and copy all files from current path into it
'''
import os
import shutil

path1 = os.path.join(os.getcwd(),'backup')
print(path1)
#os.mkdir(path1)

for val in os.listdir():
    if os.path.isfile(val):
#        print(os.path.join(os.getcwd(), val))
        shutil.copy(os.path.join(os.getcwd(), val), path1)
#        print(val)
        
'''
#command to create a new file in current directory
'''
import pathlib
pathlib.Path('newfile.txt').touch()

'''
#write a program to create a file with todays timestamp
'''
Eg: 29_jan_2019.log
29012019155323.log
'''
'''
import os
import datetime
import pathlib

path = (os.path.join(os.getcwd(),str(datetime.datetime.now().strftime('%d_%m_%Y''.log'))))

pathlib.Path(path).touch()
'''
'''
import time
filename = time.strftime('%d_%b_%Y.log')
print(filename)
pathlib.Path(filename).touch()
'''

#definition
'''
def display():
    print('inside function')
    
    
print ('program starts')
display()
print ('program end')
'''
#fixed arguments
'''
def display(first, second):
    print('inside function', first, second)
    
    
print ('program starts')
display(10,20)
print ('program end')
'''

#default arguments
'''
def display(first=0, second=0):
    final = first + second
    print(final)
    
    
print ('program starts')
display(10,20)
display (10)
print ('program end')
'''


#keyord argument

'''
def display(first, second):
    print(second)
    print(first)
    
    
print ('program starts')
display(second = 10, first = 20)
print ('program end')
'''

#variable length argument - any variable prefixed with * becomes tuple
'''
def display(*data):
    print (data)
    
display(1,2,3,4,5,6)
'''


