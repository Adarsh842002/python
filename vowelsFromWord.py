word = input("Enter a word: ")

vowels = []

for char in word:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(char)

print("List of vowels in the word:", vowels)
