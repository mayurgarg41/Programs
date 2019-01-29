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

astring = input('Input the string:')
alist = list(astring)
#for val in alist:
    


















