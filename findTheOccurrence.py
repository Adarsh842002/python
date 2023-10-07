def word_count(input_str):
    counts = dict()
    words = input_str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    print(counts)

a = input("Enter a string: ")
word_count(a)
