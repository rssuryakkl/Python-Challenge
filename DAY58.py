#Hi all This is DAY58(01-01-2024) online concert booking system
# Import the 'sub' function from the 're' module for regular expression substitution
from re import sub

# Define a function to convert a string to camel case
def camel_case(s):
    # Use regular expression substitution to replace underscores and hyphens with spaces,
    # then title case the string (capitalize the first letter of each word), and remove spaces
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    
    # Join the string, ensuring the first letter is lowercase
    return ''.join([s[0].lower(), s[1:]])

# Test the function with different input strings and print the results
cam=input("Enter a string:")
print(camel_case(cam))
