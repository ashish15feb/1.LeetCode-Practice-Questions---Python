
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    temp = []
    lengthOfnums = len(nums)
    if (lengthOfnums == k):
        return
    elif (lengthOfnums < k):
        k = k % lengthOfnums
    for i in range(k):
        temp.append(nums[lengthOfnums - k + i])
    for j in range(lengthOfnums-1, k-1, -1):
        nums[j] = nums[j-k]
    for z in range(k):
        print(nums[z])
        nums[z] = temp[z]

nums=[1,2,3]
k=1
rotate(nums, k)
print(nums)