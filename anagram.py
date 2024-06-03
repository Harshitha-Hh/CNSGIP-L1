def are_anagrams(str1, str2):
    # Remove any non-alphabetic characters and convert to lowercase
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()
    
    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted versions of the strings
    return sorted_str1 == sorted_str2

# Test the function
string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
