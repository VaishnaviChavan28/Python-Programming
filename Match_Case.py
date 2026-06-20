
# 1
ip=int(input("Enter a Number To check it is Weekday or Weekend(1-7) : "))
match ip:
    case 1 | 2 | 3 | 4 | 5 :
        print("Weekday")
    case 6 | 7 :
        print("Weekend")
    case _ :
        print("Invalid Input")


print()


# 2
payment=input("Payment Modes are : Cash/UPI/Card \n")
match payment:
    case "Cash" :
        print("Cash On delivery is Availabe")
    case "UPI":
        print("Enter UPI ID : ")
    case "Card":
        print("On Card 10% gst included")
    case _:
        print("Other payment mode is not available")

print()