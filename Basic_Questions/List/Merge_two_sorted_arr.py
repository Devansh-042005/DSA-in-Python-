nums1 = [1,2,3,4,5,6]
nums2 = [2,4,6,8,10,12]

# n = int(input("Enter count of number in arr1 : "))
# for i in range(n):
#     temp = int(input(f"Enter {i+1} number : "))
#     nums1.append(temp)

# m = int(input("Enter count of number in arr2 : "))
# for i in range(m):
#     temp = int(input(f"Enter {i+1} number : "))
#     nums2.append(temp)
n = len(nums1)
m = len(nums2)
result =[]

def merge(nums1 , nums2):
    i = 0
    j = 0

    while (i < n) and (j < m):
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or nums1[i] != result[-1] :
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if len(result) == 0 or nums2[j] != result[-1] :
                result.append(nums2[j])
            j += 1

    while i < n :
        if len(result) == 0 or nums1[i] != result[-1]:
            result.append(nums1[i])
        i += 1
    while j < m :
        if len(result) == 0 or nums2[j] != result[-1]:
            result.append(nums2[j])
        j += 1

    return result

print(merge(nums1,nums2))