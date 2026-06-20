ch=int(input("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Power\n6.Exit\nEnter Your Choice : "))

if ch==1 :
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    result=num1+num2
    print("Addition of Two Numbers is : ",result)

elif ch==2:
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    result=num1-num2
    print("Subtraction of Two Numbers is : ",result)

elif ch==3:
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    if num1>num2 and num2!=0:
        result=num1/num2
        print("Division of Two Numbers is : ",result)
    else :
        print("Unable to Perform Division Operation....")

elif ch==4:
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    if num1>0 and num2>0:
        result=num1*num2
        print("Multiplication of Two Numbers is : ",result)
    else :
        print("Unable to Perform Multiplication Operation....")

elif ch==5:
    num1=int(input("Enter 1st Number : "))
    num2=int(input("Enter 2nd Number : "))
    result=num1**num2
    print("Power of Numbers is : ",result)

elif ch==6:
    print("THANK YOU.....")
    exit()

else :
    print("Invalid Input")

        

