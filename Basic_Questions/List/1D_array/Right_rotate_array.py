nums = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    nums.append(num)

k = int(input("Enter how many time rotate array : ")) 

def rotate_array(nums , k):
    def reverse(numbs , i , j):
        while i < j:
            numbs[i],numbs[j] = numbs[j],numbs[i]
            i += 1
            j -= 1
        return numbs
    
    n = len(nums)
    reverse(nums, (n-k) , (n-1))
    reverse(nums, 0 , (n-k-1))
    reverse(nums, 0 , (n-1))
    return nums

print(rotate_array(nums,k))
