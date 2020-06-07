"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
def longestCommonPrefix(strs):
    r_str=""
    if len(strs)==0:
        return r_str
    if len(strs)==1:
        return strs[0]
    if strs[0] == '':
        return r_str
    strs.sort(key=lambda w: len(w))
    i=0
    while i < len(strs[0]):
        for word in strs:
            if strs[0][i]!=word[i]:
                return r_str
        r_str=strs[0][:i+1]
        i+=1
    return(r_str)
#longestCommonPrefix(["flower","flow","flight"])
print(longestCommonPrefix(['a','a']))
