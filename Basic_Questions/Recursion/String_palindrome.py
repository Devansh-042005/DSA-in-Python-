#  Is string is palindrome or not

input_string = input("Enter String : ")
length = len(input_string)
left = 0
right = length-1
def checking_palindrome(input_string , left , right):
    if ( input_string[left] != input_string[right]):
        return False
    if ( input_string[left] >= input_string[right]):
        return True

    return checking_palindrome (input_string , left+ 1, right-1 )

print(checking_palindrome (input_string , left , right))