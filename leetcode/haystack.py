class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            location  = haystack.find(needle)
            return location
        else:
            return -1


myobjectx = Solution()
haystack = "hello"
needle = "ll"
print myobjectx.strStr(haystack,needle)
haystack = "aaaaa"
needle = "bba"
print myobjectx.strStr(haystack,needle)

