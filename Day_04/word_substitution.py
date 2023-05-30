def substitute_word():
    str = input("Enter your string: ")
    replace_str = input("Enter word to be replaced: ")
    replace_str_by = input("Enter new word: ")
    
    new_str = str.replace(replace_str, replace_str_by)
    print(new_str)
    
substitute_word()