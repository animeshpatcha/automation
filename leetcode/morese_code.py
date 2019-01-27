#import re

class Solution(object):
    def morseCode(self, words):
        morse = []
        morseArray = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        j = 0
        morseDict = {}
        for i in range(97,123):
            morseDict[unichr(i)] = morse[j]
            j = j+1
        for k in range(0,len(words)):
            strList = list(words[k])
            morseString  = ''
            for j in range(0,len(strList)):
                morseString = morseString + morseDict[strList[j]]
            if morseString not in morseArray :
                morseArray.append(morseString)
        return morseArray

myobjectx = Solution()
words = ["gin", "zen", "gig", "msg"]
print myobjectx.morseCode(words)
