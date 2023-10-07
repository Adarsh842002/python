input_list = input("Enter a list of integers separated by spaces: ").split()

int_list = [int(num) for num in input_list]

positive_numbers = [num for num in int_list if num > 0]

print("Positive numbers from the given list:")
print(positive_numbers)
