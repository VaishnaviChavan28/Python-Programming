# print 1 to 10
print("Numbers : ")
for i in range(1,11,1): #(Starting_Value,End_Value,Increment_value)
    print(i)
print()

# Even Numbers
print("Even Numbers : ")
for i in range(0,11,2):
    print(i)

print()

# Odd Numbers
print("Odd Numbers : ")
for i in range(1,11,2):
    print(i)


print()


# Reverse Numbers
print("Reverse Numbers : ")
for i in range(10,0,-1):
    print(i)



print()

# Sum of Numbers Of Even Numbers from 1 to 10 
print("Sum of Numbers Of Even Numbers from 1 to 10 : ")
sum=0
for i in range(2,11):
    if i%2==0:
        sum+=i
print(sum)

print()

# Sum of Numbers Of Odd Numbers from 1 to 10 
print("Sum of Numbers Of Odd Numbers from 1 to 10 : ")
sum=0
for i in range(1,11):
    if i%2!=0:
        sum+=i
print(sum)

print()


# Sum of Numbers Of All Numbers from 1 to 100
print("Sum of Numbers Of All Numbers from 1 to 100 : ")
Esum=0
Osum=0
for i in range(1,101):
    if i%2==0:
        Esum+=i
    else:
        Osum+=i
print("Even Numbers Sum : ",Esum)
print("Odd  Numbers Sum : ",Osum)
print("All  Numbers Sum : ",Esum+Osum)

print()


# Printing Numbers from 1 to 100 Which Can be Divisable by 5 and 7 
print("Numbers from 1 to 100 Which Can be Divisable by 5 and 7 : ")
for i in range(1,101):
    if i%5==0 and i%7==0 :
        print(i)
    

print()

# printing 1 4 7 10
print("Random Numbers : ")
for i in range(1,11,3):
    print(i)


