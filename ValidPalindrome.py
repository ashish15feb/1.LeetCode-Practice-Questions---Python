"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    def letters(input):
        valids = ""
        for character in input:
            if character.isalnum():
                valids += character
        return valids
    @staticmethod
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """

        newS=Solution.letters(s)
        length = len(newS)
        for i in range(int((length)/2)):
            if(newS[i].lower()==newS[length-1-i].lower()):
                pass
            else:
                print(i,"--", newS[i])
                return False
        return True
print(Solution.isPalindrome("a."))