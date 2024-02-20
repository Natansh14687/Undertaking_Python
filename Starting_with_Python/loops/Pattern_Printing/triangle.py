# Printing a right angled triangle pattern using loop...
n=int(input('Enter the value of n '))
for i in range (n) :
    for j in range (i+1) :
        print("*", end=" ")
    print()