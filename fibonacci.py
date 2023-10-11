num=int(input("Enter the number of elements"))
a=int(input("Enter the first elements"))
b=int(input("Enter the second elements"))
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)
