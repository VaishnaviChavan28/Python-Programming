
# 1 :- 
num=int(input("Enter a Number : "))
if num>0 :
    print("Number is Positive")
elif num<0 :
    print("Number is Negative")
elif num==0 :
    print("Number is Zero")
else :
    print("Invalid Number")

print()


# 2 :- 
age=int(input("Enter Your Age : "))
if age>=1 and age<=18 :
    print("Your are Childern")
elif age>=19 and age<=30 :
    print("Your are Teenager")
else :
    print("Your are Adult")

print()


# 3 :- 
marks=int(input("Enter Marks :  "))
if marks>=0 and marks<=35 :
    print("Poor Performance")
elif marks>=36 and marks<=65 :
    print("Good Performance")
elif marks>=66 and marks>=100 :
    print("Excellent Performace") 
else :
    print("Invalid Marks")

print()




# 4 :-
signal=input("Enter Signal (r/y/g) : ")
if signal=='r'or signal=='R':
    print("STOP")
elif signal=='y' or signal=='Y' :
    print("Go Slow")
elif signal=='g' or signal=='G' :
    print("Go")
else :
    print("Invalid Input")


print()