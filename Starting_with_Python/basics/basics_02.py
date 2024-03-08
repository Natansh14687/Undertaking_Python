# Tuples
tup1 = tuple()
print(type(tup1))
print(tup1)

tup2 = tuple("Natansh")
print(tup2)

tup3 = (1)
print(type(tup3))
tup3 = (1,)
print(type(tup3))

tup4 = (1,2,3,4,5,1,1,3,1,4,2,1)
print(tup4.count(1))
print(len(tup4))

# Dictionary
dic = dict(name = "Natansh", age = 20)
print(dic)
print(type(dic))

dic1 = {"Name":"Natansh","Name1":"Dushyant"}
print(dic1)

# set
s = {1,2,3,2,3,2,3,1,4,5,4,5}
print(s)
print()
# ------------------------------------------------------------------------------------

print(float('inf'))
print(float("nan"))
print(float("-inf"))

print(float("inf")>float("nan"))

# Conditions

x = 10
if x > 7:
    print("Yeahhhhhh")
else:
    print("nope")

print()

# grade = int(input("Enter your grade : "))
# if grade >= 90:
#     print("Excellent")
# elif grade >= 80:
#     print("Well done!!")
# elif grade >= 50:
#     print("pass")
# else:
#     print("fail")


num = 5
result = "yeahhh" if num > 2 else "false"
print(result)
