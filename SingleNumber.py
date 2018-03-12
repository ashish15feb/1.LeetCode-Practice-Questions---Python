"""
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
        """
    """
    numbers={}
    for i in range(len(nums)):
        if nums[i] not in numbers:
            numbers[nums[i]]=1
        else:
            numbers[nums[i]]=2
    for key in numbers:
        if numbers[key]==1:
            return key
    """
    a=0
    for i in nums:
        a ^= i
        print(a)
    return a

nums=[1,2,3,4,1,2,3]
print(singleNumber(nums))