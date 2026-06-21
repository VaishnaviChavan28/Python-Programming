# List Creation In python
rollno=[101,102,103]
print(rollno)

# access Variable name using index no.
print(rollno[0])

# update list
rollno[2]=107
print(rollno)


print()
print("======================================================")
print()

student_name=["abc","xyz","pqr","mno"]
print(student_name)

# positive indexing is allowed in list which is left to right
print(student_name[1])
# negative indexing is also allowed in list which is right to left
print(student_name[-1])

print()
print("======================================================")
print()

# mixed values in list
mixed=[1.90,90,"ram",889.0]
print(mixed)
print(mixed[2])
print(mixed[-2])

print()
print("======================================================")
print()

# we can change the string value inside list because list is mutable
mixed[2]="Ramesh"
print(mixed)
print(type(mixed))

print()
print("======================================================")
print()

# list loop
for i in mixed:print(i)

print()
print("======================================================")
print()

x=[10,20,30,40]
print(10 in x)
print(90 in x)

# inbuilt methods of list
# add :- 1) append :- add the value at the last index of list
        # 2) insert(indexno,value):- add the value on the mentioned index
x.append(60)
print(x)
x.insert(2,100)
print(x)


print()
print("======================================================")
print()

# remove :- 1)remove(element) :-delete the value from the list using direct value/element
#   2)pop(index) : -delete the value using the index
x.remove(20)
print(x)
x.pop(4)
print(x)

print()
print("======================================================")
print()

a=[10,20,30,40,90,70]
print(a)

# new -- last index
a.append(100)
print(a)

print()
print("======================================================")
print()

# index -- value add
a.insert(1,99)
print(a)

print()
print("======================================================")
print()

# last index -- remove
a.pop()
print(a)

print()
print("======================================================")
print()

# value remove
a.remove(90)
print(a)

print()
print("======================================================")
print()

# list --clear
a.clear()
print(a)

print()
print("======================================================")
print()

x=[1,2]
y=[3,4]
print(x)
# add on x
x.extend(y)
print(x)

# returns the index of element/value in the list
# syntax :- varname.index(value)
print(x.index(2))

print()
print("======================================================")
print()


print("Reverse a List : ")
x=[10,20,30,40,50]
x.reverse()
print(x)
print()

print("Copy a List : ")
a=[10,20,30]
b=a.copy()
print(b)
print()

print("Sort a List(ascending order ) : ")
x=[90,70,50,30,100]
x.sort()
print(x)
print()


print("Sort a List(descending order ) : ")
x.sort(reverse=True)
print(x)
print()

print("no. of element occurs in the list : ")
x=[11,33,444,444,11,22]
print(x.count(11))
print()

# in-bulit function
print(max(x)) 
print(min(x)) 
print(sum(x)) 
print(len(x)) 
print()

print("Sum of values of a list : ")
x=[10,20,30,40]
sum=0
for i in x:
    sum+=i
print(sum)
print()


print("Maximum Value Of List : ")
x=[10,20,30,40]
max=0
for i in x:
    if i>max:
        max=i
print(max)
print()

print("Reversing a List")
x=[10,20,30,40,89,10,100]
rev=[]
for i in range (len(x)-1,-1,-1):
    rev.append(x[i])
print(rev)

print()


print("Replace a value with Zero")
x=[10,20,30,40,89,10,100]
for i in range(len(x)):
    if x[i]==30:
        x[i]=0
print(x)

print()

print("Finding Unique Values From a list")
x=[21,23,24,21,25,25]
uni_element=[]
for i in x:
    if i not in uni_element:
        uni_element.append(i)
print(uni_element)

print()


print("Finding Square and Cube of a number which is divided by five ")
x=[24,56,78,97,30]
sq=0
for i in x:
    if i%5==0:
        sq=i**2
print(sq)
print(sq**3)

print()


