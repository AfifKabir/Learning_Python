#1+2+3+...+n
'''
n=int(input("Enter the number:"))
sum=0
for x in range(1,n+1,1) :
    sum=sum+x
print(sum)
'''
'''
#2+4+...+n
n=int(input("Enter the number:"))
sum=0
for x in range(2,n+1,2) :
    sum=sum+x
print(sum)
'''
'''
#1+3+...+n
n=int(input("Enter the number:"))
sum=0
for x in range(1,n+1,2) :
    sum=sum+x
print(sum)
'''
'''
#4+8+12+...+n
n=int(input("Enter the number:"))
sum=0
for x in range(4,n+1,4) :
    sum=sum+x
print(sum)
'''
'''
#1*1+2*2+...+n*n
n=int(input("Enter the number:"))
sum=0
for x in range(1,n+1,1) :
    sum=sum+x*x
print(sum)
'''
'''
#1+1/2+...+1/n
n=int(input("Enter the number:"))
sum=0
for x in range(1,n+1) :
    sum=sum+(1/x)
print(sum)
'''
'''
#2 x 4 x ...xn
n=int(input("Enter the number:"))
mul=1
for x in range(2,n+1,2) :
    mul=mul*x
print(mul)
'''
'''
#1 x 3 x 5 x...x n
n=int(input("Enter the number:"))
mul=1
for x in range(1,n+1,2) :
    mul=mul*x
print(mul)
'''
'''
#4x8x...xn
n=int(input("Enter the number:"))
mul=1
for x in range(4,n+1,4) :
    mul=mul*x
print(mul)
'''
#1*1 x 2*2 x ...xn*n
n=int(input("Enter the number:"))
mul=1
for x in range(1,n+1,1) :
    mul=mul*x*x
print(mul)