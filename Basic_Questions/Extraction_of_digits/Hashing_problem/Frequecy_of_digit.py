# Calculate the frequency of given numbers in an array and return frequency in a list 

numbers = [1, 2, 1, 4, 4, 7, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9]
given_number = [111, 23, 2, 3, 1, 5]
temp_list = []
frequency_count = [0] * (max(numbers)+1)
for i in numbers:
    if (i in frequency_count):
        frequency_count[i] = frequency_count[i] + 1 
    else :
        frequency_count[i] = 1

        
for i in given_number :
    if (i < (max(numbers)+1)):
        temp_list.append (frequency_count[i])
    else :
        temp_list.append (0)

print("Frequency of a given array's number : " ,temp_list)

