# Write a program to check if a number is a palindrome.

def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

# Example usage
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")