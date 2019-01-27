#import re

class Solution(object):
    def toLowerCase(self, str):
        lowerChar = ''
        mychar = list(str)
        for j in range(0,len(str)):
            if ((ord(mychar[j]) > 64)  and  (ord(mychar[j]) < 91)):
                lowerChar = lowerChar  + chr(ord(mychar[j]) + 32)
            else:
                lowerChar = lowerChar  + chr(ord(mychar[j]))
        return lowerChar

myobjectx = Solution()
print myobjectx.toLowerCase('HelLo World')
