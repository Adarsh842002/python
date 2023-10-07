
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if len(string1) < 2 or len(string2) < 2:
    print("Both strings should have at least 2 characters.")
else:

    swapped_string1 = string2[0] + string1[1:]
    swapped_string2 = string1[0] + string2[1:]

  
    result_string = swapped_string1 + " " + swapped_string2

 
    print("Result:", result_string)
