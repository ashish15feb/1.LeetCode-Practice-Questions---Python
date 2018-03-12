"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number=defaultdict(int)
        flag=False
        for i in range (len(nums)):
            if number[nums[i]]==1:
                flag=True
                break
            else:
                number[nums[i]]=1
        if flag==True:
            return True
        return False