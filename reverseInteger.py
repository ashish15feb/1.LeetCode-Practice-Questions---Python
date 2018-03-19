"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within
the 32-bit signed integer range. For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.
"""

class Solution:
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """

        intList=[]
        thisInteger=x
        if(x<0):
            thisInteger=thisInteger*(-1)
        while(thisInteger!=0):
            reminder=thisInteger%10
            intList.append(reminder)
            thisInteger=int(thisInteger/10)
        thisInteger=0
        for i in range (len(intList)):
            thisInteger=thisInteger*10+intList[len(intList)-1-i]
        if (thisInteger > 2147483647 or thisInteger < -2147483649):
            return 0
        if(x<0):
            return thisInteger*(-1)
        return thisInteger

print(Solution.reverse(-123))