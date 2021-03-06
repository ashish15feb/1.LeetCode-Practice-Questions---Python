"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def convertString(self, n):
        string = str(n)
        outString = ''
        count = 1
        for i in range(len(n)):
            if (i + 1 < len(n) and (string[i] == string[i + 1])):
                count = count + 1
            else:
                outString = outString + str(count)
                outString = outString + string[i]
                count = 1
        return outString

    def recursive(self, n):
        if(n==1):
            return str(1)
        else:
            thisString=self.recursive(n-1)
            count = 1
            outString=''
            for i in range(len(thisString)):
                if (i + 1 < len(thisString) and (thisString[i] == thisString[i + 1])):
                    count = count + 1
                else:
                    outString = outString + str(count)
                    outString = outString + thisString[i]
                    count = 1
            return outString

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = str(1)
        for i in range(2, n + 1):
            base = self.convertString(base)
        return base

this=Solution()
print(this.countAndSay(5))
print(this.recursive(5))