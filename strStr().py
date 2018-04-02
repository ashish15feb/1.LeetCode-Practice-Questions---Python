"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    @staticmethod
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Bruteforce
        """
        i=0
        j=0
        pointer=-1
        if ((len(haystack) == 0 and len(needle) == 0) or (len(haystack) >0 and len(needle) == 0)):
            return 0
        if(len(haystack) == 0 and len(needle)>0):
            return -1
        while(i<len(haystack)):
            if(haystack[i]==needle[0]):
                pointer=i
                while(j<len(needle)):
                    print(i,j)
                    if(i<len(haystack) and haystack[i]==needle[j]):
                        i=i+1
                        j=j+1
                    else:
                        i=pointer
                        pointer=-1
                        j=0
                        break
            if(pointer!=-1):
                break
            i=i+1
        return pointer
        """

        i = 0
        if (len(needle) == 0):
            return 0
        while (i < len(haystack) - len(needle) + 1):
            if (haystack[i] == needle[0]):
                #print(haystack[i:i + len(needle)])
                if (haystack[i:i + len(needle)] == needle):
                    return i
            i = i + 1
        return -1
print(Solution.strStr("aaab", "ab"))