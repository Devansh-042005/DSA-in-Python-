# Give fibonacci  number
number = int(input("Enter nth number of palindrome series : "))
def checking_palindrome(number):
    if (number == 0 or number == 1):
        return number

    return checking_palindrome(number-1) + checking_palindrome(number-2)

print(checking_palindrome(number))