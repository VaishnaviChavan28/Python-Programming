# Sum of a Number
num=1234
sum=0
i=1
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print("Sum of Number is : ",sum)

print()

# Check Number is Palindrome or not
num=1212
rev=0
temp=num
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num//=10

if temp==rev:
    print("Number Is Panlindrome")
else:
    print("Number Is Not Panlindrome")

print()

# Finding Factors of a Number
num=int(input("Enter a Number To Its Factors : "))
i=1
print("Factors Of Number Are : ")
while i<=num:
    if num%i==0:
        print(i)
    i+=1

print()

# Finding Factorial of a number
num=int(input("Enter a Number To Its Factorial : "))
i=1
fact=1
print("Factorial Of Number is : ")
while i<=num:
    fact*=i
    i+=1
print(fact)


print()


# Finding Count Of Digit
num=int(input("Enter a Number To to Count its digit : "))
ct=0
print("Count Of a Digit is : ")
while num>0:
    ct+=1
    num//=10
print(ct)

print()


# Finding Number is Happy or Sad
num=int(input("Enter a Number To Check It is Happy or Sad  : "))
while num!=1 and num!=4 :
    sum=0
    while num>0:
        rem=num%10
        sum+=rem*rem
        num//=10
    num=sum
if num==1:
    print("It is Happy Number")
else:
    print("It is Sad Number")

print()


# Finding Number is ArmStrong or Not
num=int(input("Enter a Number To Check It is ArmStrong or Not  : "))
ct=0
sum=0
temp=num
while num>0:
    ct+=1
    num//=10
print(ct)
num=temp
while num>0:
    rem=num%10
    sum+=rem**ct
    num//=10
if temp==sum:
    print("It is ArmStrong..")
else:
    print("It is Not ArmStrong..")


print()

# Finding Number is Perfect or Not
num=int(input("Enter a Number To Check It is Perfect or Not  : "))
sum=0
i=1
while i<num:
    if num%i==0:
        sum+=i
    i+=1
print(sum)
if num==sum:
    print("Number is Perfect...")
else:
    print("Number is Not Perfect..")


# Check the Number is Prime or not
num=int(input("Enter a Number To Check It is Prime or not  : "))
i=2
is_prime=True

if num<=1:
    is_prime=False
else:
    while i<=num//2:
        if num%i==0:
            is_prime=False
            break
        i+=1

if is_prime:
    print("Number is Prime")
else:
    print("Number is Not Prime")


print()


# Printing the Fibonacci Series of the terms
terms=int(input("Enter The number of terms for Fibonacci Series : "))
n1=0
n2=1
ct=0

print("Fibonacci Series: ")
if terms<=0:
    print("Please Enter a Positive Integer")
elif terms==1:
    print(n1)
else:
    while ct<terms:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        ct+=1
print()


print()


# Check the number is Neon or not

num=int(input("Enter a Number To Check It is Neon or not  : "))
square=num*num
sum_of_digits=0


while square>0:
    rem=square%10
    sum_of_digits+=rem
    square//=10


if sum_of_digits==num:
    print("It is a Neon Number")
else:
    print("It is Not a Neon Number")

