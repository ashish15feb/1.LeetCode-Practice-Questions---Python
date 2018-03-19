"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Below solution is using for loops
        """
        for i in range(len(s)):
            count=0
            for j in range(0, len(s)):
                if(s[j]==s[i]):
                    count=count+1
                if(count>1):
                    break
            if(count==1):
                return i
        return -1
        """
        #Below solution is using Hashmap
        hmap = {}
        for i in range(len(s)):
            if (s[i] in hmap.keys()):
                if (hmap[s[i]] != 1):
                    hmap[s[i]] = 1
            else:
                hmap[s[i]] = 0
        for i in s:
            if (hmap[i] == 0):
                return s.index(i)
        return -1