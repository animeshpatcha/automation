'''
Write a function that takes a string as input and returns the string reversed.

Example 1:

    Input: "hello"
    Output: "olleh"

    Example 2:

    Input: "A man, a plan, a canal: Panama"
    Output: "amanaP :lanac a ,nalp a ,nam A"


'''
import re
class Solution(object):
    def reverseString(self, s):
        reverse_word_array = []
        reverse_string_array = []
        if ((len(s) - len(s.strip())) == len(s)):
            return ' '.join(s)
        lstrip_cnt = len(s) - len(s.lstrip())
        rstrip_wspace = ""
        for n in range (0,lstrip_cnt):
            rstrip_wspace = rstrip_wspace + " "
        rstrip_cnt = len(s) - len(s.rstrip())
        lstrip_wspace = ""
        for n in range (0,rstrip_cnt):
            lstrip_wspace = lstrip_wspace + " "
        word_array = re.split(r"(\s+)",s)
        if len(word_array) > 1:
            i = len(word_array) - 1
            for j in range(0, len(word_array)):
                reverse_word_array.append(word_array[i])
                i = i-1
        else:
            reverse_word_array.append(word_array[0])
        for j in range(0,len(reverse_word_array)):
            reverse_sarray = list(reverse_word_array[j])
            i = len(reverse_sarray) - 1
            for k in range(0,len(reverse_sarray)):
                reverse_string_array.append(reverse_sarray[i])
                i = i - 1
        final_string_1 = ''.join(reverse_string_array)
        final_string_2 = final_string_1.rstrip()
        final_string = lstrip_wspace + final_string_2 + rstrip_wspace
        return final_string


myobjectx = Solution()
words = "A man, a plan, a canal: Panama"
print myobjectx.reverseString(words)
words = " "
print myobjectx.reverseString(words)
words = "Panama"
print myobjectx.reverseString(words)
words = "0z;z   ; 0"
print myobjectx.reverseString(words)
