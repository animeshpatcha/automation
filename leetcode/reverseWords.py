'''
Given an input string, reverse the string word by word.

Example:

    Input: "the sky is blue",
    Output: "blue is sky the".
    Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.
'''

class Solution(object):
    def reverseWords(self, s):

        listOfString = s.split()
        rstring = ''
        for j in range(len(listOfString)-1,-1,-1):
            rstring += listOfString[j] + ' '
        return rstring.strip()


myobjectx = Solution()
target= "  the  world  is your oyester "
print myobjectx.reverseWords(target)
