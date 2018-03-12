"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        zeroCount=0
        while(i<(len(nums))):
            if(nums[i]==0):
                nums.pop(i)
                zeroCount=zeroCount+1
                i=i-1
            i=i+1
        while(zeroCount>0):
            nums.append(0)
            zeroCount=zeroCount-1
        return nums

num=[0,1,0,3,12]
print(Solution.moveZeroes(num))