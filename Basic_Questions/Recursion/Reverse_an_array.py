arr = []
input_size = int(input("Enter count of number : "))

for i in range (0 , input_size):
    temp_var = int(input("Enter digit : "))
    arr.append (temp_var)
print(arr)
print ("Reverse an array : ")
left = 0
right = len(arr) - 1

def reverse_array (array , left , right):
    if left >= right :
        return array
    array[left] , array[right] = array[right] , array[left] 
    return reverse_array (array , left+1 , right-1)

result = reverse_array(arr , left , right)
print(result)