
list1 = list(map(int, input("Enter the first list of integers (comma-separated): ").split(',')))
list2 = list(map(int, input("Enter the second list of integers (comma-separated): ").split(',')))


if len(list1) == len(list2):
    print("The lists are of the same length.")
else:
    print("The lists are of different lengths.")


if sum(list1) == sum(list2):
    print("The lists sum to the same value.")
else:
    print("The lists do not sum to the same value.")


common_elements = set(list1) & set(list2)
if common_elements:
    print("Common elements in both lists:", common_elements)
else:
    print("There are no common elements in both lists.")
