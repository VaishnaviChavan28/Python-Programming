
print("Nested Loop")
x=[[1,2,3],[4,5,6],[7,8,9]]
print(x)
print()

print("Type of Variable X : ",type(x))
print()

print("access sublist element")
print(x[1])
print()

print("Access particular element of a sublist")
print(x[2][1])
print()

print("Access Sublist")
for i in x:
    print(i)
print()

print("Access All Particular element of a sublist ")
for row in x:
    for col in row:
        print(col,end=" ")
print()

print()


print("Update a value in a list")
x[1][1]=1000
print(x)
print()

print("Student Record")
student=[["Amit",90],["Ram",70],["Sita",80]]
print(student)
print()

# Customize Output
for row in student:
    print(f"Student Name : {row[0]} , Marks : {row[1]}")
print()


print("Printing the sum of marks")
sum=0
for marks in student:
    sum+=marks[1]
print(sum)
print()

print("Display the name of student who got the marks above 80")
for marks in student:
    if marks[1]>80:
        print("Student Name : ",marks[0])
print()


print("Replace Even Marks with 0 and Odd Marks with 1")
student=[["Amit",90],["Ram",89],["Sita",67]]
for row in student:
    if row[1]%2==0:
        row[1]=0
    else:
        row[1]=1
print(student)
print()

print("Add Element to list")
student.append(["Payal",99])
student.append(400)
print(student)
print()

print("Access Particular value")
print(student[1])
print(student[2][0])
print(student[4])
print()

