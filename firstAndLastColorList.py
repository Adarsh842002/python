
color_input = input("Enter comma-separated color names: ")


color_list = color_input.split(',')


if color_list:
   
    first_color = color_list[0].strip() 
    last_color = color_list[-1].strip()  
    
    print("First color:", first_color)
    print("Last color:", last_color)
else:
    print("The list of colors is empty.")
