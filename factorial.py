num=int(input("Enter the number:"))
f=1
if num==0:
    print("The factorial of zero is:",f)
elif num<0:
    print("The factorial cannot be found")
else:
    for i in range(1,num+1):
        f=f*i
    print("The factorial of",num," is", f)
