# 1
num=4
i=1
while i<=num:
    j=1
    while j<=num:
        print("*",end=" ")
        j+=1
    print()
    i+=1

print()

# 2
num=3
i=1
no=1
while i<=num:
    j=1
    while j<=num:
        print(no,end="  ")
        j+=1
        no+=1
    print()
    i+=1

print()

# 3
num=4
i=1
while i<=num:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()

print()

# 4
num=4
i=num
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i-=1
    print()

print()



# Similarly
for i in range (num,0,-1):
    print("* "*i)

print()



# 5
n=4
i=1
while i<=n:
    k=1  #Spaces
    while k<=n-i:
        print(" ",end=" ")
        k+=1
    j=1 #Star
    while j<=i:
        print( "*",end=" ")
        j+=1
    print()
    i+=1

print()



# 6
n=4
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i+=1

print()



# Similary
n=4
for i in range (1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()


print()



# 7
n=4
i=n
while i>=1:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i-=1

print()



# Similarly
n=4
for i in range(n,0,-1):
    for k in range (1,n+1-i):
        print(" ",end="")
    for j in range (0,2*i-1):
        print("*",end="")
    print()

print()



# 8
n=4
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i+=1
n=4
i=n-1
while i>=1:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i-=1

print()



# Similarly
n=4
for i in range (1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for k in range (1,n+1-i):
        print(" ",end="")
    for j in range (0,2*i-1):
        print("*",end="")
    print()



print()


# 9
n=4
i=n
while i>=1:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i-=1
n=4
i=2
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
    print()
    i+=1

print()

# 10
n=5
for i in range (1,n+1):
    for  k in range (1,i+1):
        print("*",end="")
    for j in range(1,2*(n-i)+1):
        print(" ",end="")
    for m in range (0,i):
        print("*",end="")
    print()

for i in range (n-1,0,-1):
    for  k in range (1,i+1):
        print("*",end="")
    for j in range(1,2*(n-i)+1):
        print(" ",end="")
    for m in range (0,i):
        print("*",end="")
    print()

print()
