"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    @staticmethod
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charIndex=[0]*128
        for i in s:
            charIndex[ord(i)] = charIndex[ord(i)] + 1
        for i in t:
            charIndex[ord(i)] = charIndex[ord(i)] - 1
        for i in range(128):
            if (charIndex[i]!=0):
                #print(charIndex[i],"---", i)
                return False
        return True
print(Solution.isAnagram("ab","bb"))