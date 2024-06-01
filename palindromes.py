def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Reverse the cleaned string
    reversed_string = cleaned_string[::-1]
    
    # Check if the original cleaned string is equal to the reversed string
    return cleaned_string == reversed_string

# Get input from the user
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
