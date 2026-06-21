# String Formating 
fname ="Vaishnavi"
mname="Vijay"
lname="Chavan"
print("Firstname : ",fname,"\nMiddlename : ",mname,"\nLastname : ",lname)
print(f"Fname : {fname}\nMname : {mname}\nLname : {lname}")
print()

# String inbuilt Methods
country="India"
print(country.lower())
print(country.upper())
print()

a="HELLO"
print(a.islower())
print(a.isupper())
print()

x="india is my country"
print(x.title())
print(x.capitalize())
print()

s="PYTHON"
if s.isupper():
    print("It is UpperCase")
else:
    print("It is LowerCase")
print()

x="HeLlo"
print(x.swapcase()) # convert uppercase to lower and viceversa
print(len(x)) #returns the length of the string
print(x.find('e')) #returns index number if letter is present in the string
print(x.find('v')) #returns -1 if letter is not present in the string
print(x.index('o')) #returns index number if letter is present in the string otherwise returns error
print(x.count('L')) #count the appeared numbers of a letter in the string
print()

# Fetching String Letter one by one
city="Pune"
for i in city:
    print(i,end="  ")
print()

print()

# Printing Vowels from the string
state="Education"
for i in state:
    if i in 'aeiouAEIOU':
        print(i)
print()

# Count no. of Vowels in the string
x="india"
ct=0
for ch in x:
    if ch in 'aeiouAEIOU':
        ct+=1
print(ct)

print()

# true/false ->>> Inbuilt Method Checking...
x="abc123"
print(x.isalpha())#returns true only if a string contains alphabets otherwise return false
print(x.isnumeric())#returns true only if a string contains numbers otherwise return false
print(x.isalnum())#returns true only if a string contains numbers and alphabets otherwise return false

print()

y="abc"
print(y.isalpha())

print()

z="12345"
print(z.isnumeric())

print()


# String --->> startswith / endswith
a="python"
print(a.startswith('pyt'))
print(a.startswith('y'))
print(a.endswith('n'))
print((a.replace('p' , 'P')))
print((a.replace('t' , 'P')))

print()

# count the no. of letters in a string without using len() method
x="stringLetter"
ct=0
for ch in x:
    ct+=1
print(ct)

print()

# Reversing a string
x="Hello"
print(x[::-1])


print()

# Check the string is palindrome or not
# x=input("Enter a String : ")
x="wow"
y=x[::-1]
if x==y:
    print("Given String is palindrome")
else:
    print("Given String is not palindrome")
print()

# Replace letter of string without using replace() method
x="Maharashtra"
op=""
for ch in x:
    if ch=='a':
        op+='x'
    else:
        op+=ch
print(op)

print()

# Swap the case of letters in the string without swapcase() method
x="HeLlO"
op=""
for ch in x:
    if ch.islower():
        op+=ch.upper()
    else : 
        op+=ch.lower()
print(op)

print()


# Find the duplicate letters of a string
x="maharashtra"
for ch in set(x):
    if x.count(ch)>1:
        print(ch)
    
print()

# Reverse a string without built in method
x="Hello"
rev="" 
for ch in x:
    rev=ch+rev
print(rev)

print()

# duplicate character remove 
z="hello"
op="" 
for ch in z:
    if ch not in op:
        op+=ch
print(op)

print()

# Count no. of words in a sentence
a="I,Like,Python,Programming"
print(a)
words=a.split(",")
print(words)
print(len(words))

print()

st1="python_is_easy_to_learn"
words=st1.split("_")
print(len(words))

print()

# Find the largest word in string
str2="python is interpreted language"
words=str2.split()
largest_word=""
for ch in words :
    if len(ch)>len(largest_word):
        largest_word=ch
print(largest_word) 

print()

str3="hello"
freq={}
for ch in str3:
    if ch in freq :
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

print()



