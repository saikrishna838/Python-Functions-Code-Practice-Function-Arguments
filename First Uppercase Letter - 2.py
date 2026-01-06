def get_first_upper_letter(string):
    
    for each_char in string:
        if each_char == each_char.upper():
            first_upper_case_letter = each_char
            break
    return first_upper_case_letter
      


string = input()
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)