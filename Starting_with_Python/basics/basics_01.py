name = "Natansh" # same location shown for both variable and its value.
print(id(name))
print(id("Natansh"))
print()

a,b,c,d,e = 1,2,3,4,5 # way to define multiple variables in a line.
print(d)
print()

# print(input("What is your name : "))
# n = int(input("Enter any number : "))
# print(n)
# n2 = str(input("Enter any string : "))
# print(n2)
# print(type(n2))

print("First number is : ",a," and second number is : ",b) #Combined printing
print(f'First number is {a} and second number is {b}') #formatted string printing
print("First number is {} and second number is {}".format(a,b)) # format method for string printing.

print("My name is Natansh",a,b,c, sep="%")
print(1,end="..")
print(2,end="@")
print(3,end="-")
print(4)

print()

s = "Natansh"
print(s[1])
print(s[6])
print(s[0])
print(s[0:7])
print(s[-1:0:-1])
print(s[0:7:2])

print()

q = "Natansh Khurana"
print(len(q))
print(q.upper())
print(q.capitalize())
str1 = "Natansh"
str2 = " Khurana"
print(str1 + str2)
print(q.lower())

print()

str3 = "              Natansh Khurana         "
print(str3)
print(str3.strip())
print(id(str3.strip()))
print(id(str3))
str4 = "Natansh1"
str4= "Khurana"
print(str4)
print(id("Natansh1"))
print(id("Khurana"))
print(id(str4))

# str1[0]="i" # string does not support item assignment means strings are immutable.
# print(str1)

ls = list()
print(ls)
x = [1,2,3]
y = [1,2,3]
print(x==y)
print(id(x))
print(id(y))

ls1 = list("Natansh ji")
print(ls1)

import sys
num = 1
print(sys.getsizeof(num))

lst = list()
print(sys.getsizeof(lst))

lst1 = [1,2,4,5]
lst1.append(6)
print(lst1)

lst1.insert(1,9)
print(lst1)

lst1.extend([7,6,5,4])
print(lst1)
lst1.extend(ls1)
print(lst1)

lst1.remove(4)
print(lst1)

lst1.pop(1)
print(lst1)

lst1.pop()
print(lst1)

print()
print()

arr1 = [1,2,3,4,5]
arr1.reverse()
print(arr1)

print()

arr2=arr1.copy()
print(arr2)
print(id(arr1))
print(id(arr2))

print()

arr = [12,67,54,23,12]
arr.sort()
print(arr)

