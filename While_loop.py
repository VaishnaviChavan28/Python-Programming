# Print HelloWorld for more than 1 time
i=1
print("Repeatation Of Word ")
while i<=3 :
    print(i,"Hello World")
    i+=1

print()

# Print Numbers From 1 to 20
i=1
print("Numbers From 1 to 20 Are : ")
while i<=20 :
    print(i)
    i+=1

print()

# Print Odd Numbers from 1 to 20
i=1
print("Odd Numbers Are : ")
while i<=10:
    if i%2!=0:
        print(i)
    i+=1

print()

# Print Even Numbers from 1 to 20
i=1
print("Even Numbers Are : ")
while i<=10:
    if i%2==0:
        print(i)
    i+=1

print()


# Reverse Number Printing from 10 to 1
i=10
print("Reverse Numbers Printing From 10 to 1")
while i>=1:
    print(i)
    i-=1


print()

# Sum of all numbers from 1 to 20
i=1
sum=0
while i<=20:
    sum+=i
    i+=1
print("Sum of all numbers from 1 to 20 is : ",sum)

print()

# Sum of Even  Numbers from 1 to 50
i=0
sum=0
while i<=50:
    if i%2==0:
        sum+=i
    i+=1
print("Sum of all even numbers from 1 to 50 is : ",sum)

print()


# Sum of Odd Numbers from 1 to 50
i=0
sum=0
while i<=50:
    if i%2!=0:
        sum+=i
    i+=1
print("Sum of all odd numbers from 1 to 50 is : ",sum)


print()

# Sum of All Even and Odd Numbers from 1 to 50
i=1
evenSum=0
oddSum=0
while i<=50:
    if i%2==0:
        evenSum+=i
    else :
        oddSum+=i
    i+=1
print("Even Number Sum : ",evenSum)
print("Odd Number Sum : ",oddSum)
print("ALL Number Sum : ",evenSum+oddSum)

print()

# Printing the Numbers which are divisible by 5 and 7 from 1 to 100
i=1
print("Printing the Numbers which are divisible by 5 and 7 from 1 to 100")
while i<=100 :
    if i%5==0 and i%7==0:
        print(i)
    i+=1

print()

# Printing Table Of Five 
i=1
num=5
print("Table Of Five")
while i<=10:
    print(num," X ",i," = ",num*i)
    i+=1

print()

# Print A to Z Alphabets
# ord() :- convert char to ascii
# chr() :- convert ascii to char
# A to Z :- 65 to 90
# a to z :- 97 to 122
i=ord('A')  #65
print("Capital Alphabets : ")
while i<=ord('Z'):
    print(chr(i),end=" ")
    i+=1  
i=ord('a')  #97
print("\n")
print("Small Alphabets : ")
while i<=ord('z'):
    print(chr(i),end=" ")
    i+=1


print()

# Reverse Order of Alphabets

i=ord('Z')  #65
print("\n")
print("Capital Alphabets : ")
while i>=ord('A'):
    print(chr(i),end=" ")
    i-=1  
i=ord('z')  #97
print("\n")
print("Small Alphabets : ")
while i>=ord('a'):
    print(chr(i),end=" ")
    i-=1


print()