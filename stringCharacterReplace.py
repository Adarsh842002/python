
input_string = input("Enter a string: ")


first_char = input_string[0]


replaced_string = first_char + input_string[1:].replace(first_char, '$')


print("Modified string:", replaced_string)
