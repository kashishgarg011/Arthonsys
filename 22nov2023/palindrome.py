#1. Check if a given string is a palindrome or not.
first_str=input('Enter a string:')
second_str=first_str[::-1]
if first_str==second_str:
    print('Given string is a palindrome')
else:
    print('Given string is not a palindrome')