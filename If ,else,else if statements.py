#Pass/Fail
num=int(input("Enter the number:"))
if num >= 33 :
    print("Pass")
else :
    print("Fail")

#Largest number by nested if-else statements
num1=20
num2=10
num3=-10
if num1>num2 :
    if num1>num3:
        print(num1)
    else :
        print(num3)
elif num2>num1 :
    if num2>num3 :
        print(num2)
    else :
        print(num3)
    

