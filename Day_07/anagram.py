# Check two strings are anagrams
# Anagrams are string strings with the same characters in different order

def check_anagram(str1, str2):
    
    # Remove empty spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # print(str1, str2)
    # print(sorted(str1))
    # print(sorted(str2))
    
    # Sort characters and compare them
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")
    
string1 = "listen 2"
string2 = "silent 1"

check_anagram(string1, string2)