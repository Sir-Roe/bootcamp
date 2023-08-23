'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letter
'''


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
     """
  

    return

strs = ["eat","tea","tan","ate","nat","bat"]
strs.sort()
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True 

for i in range(len(strs)-1):
    for j in range(i,len(strs)):
        if isAnagram(i,j)==True:
