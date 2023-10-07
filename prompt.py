
num_elements = int(input("How many elements do you want to enter: "))

my_list = []

for i in range(num_elements):
    value = int(input(f"Enter element {i + 1}: "))
    if value > 100:
        my_list.append('over')
    else:
        my_list.append(value)

print("Modified list:", my_list)
