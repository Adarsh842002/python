
names_list = []


num_names = int(input("How many names do you want to store? "))

for i in range(num_names):
    name = input(f"Enter name {i + 1}: ")
    names_list.append(name)


count_a = 0
for name in names_list:
    count_a += name.lower().count("a")


print(f"The letter 'a' occurs {count_a} times within the list of names.")
