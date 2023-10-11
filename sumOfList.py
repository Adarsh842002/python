
n=int(input("Enter the number of elements in list"))
my_list = []
for i in range(n):
      e=int(input(f"Enter the element {i+1}:"))
      my_list.append(e)
sum = 0
for i in range(len(my_list)):
               sum = sum + my_list[i]
print("Sum of elements in list:",sum)
