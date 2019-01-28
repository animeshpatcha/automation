'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

class Solution(object):
    def longestConsecutive(self, numArray):

        sortedArray = sorted(numArray)
        print sortedArray
        myStreak = 0
        longest=0
        for i in range(0,len(sortedArray)-1):
            if sortedArray[i] == sortedArray[i+1] - 1:
                myStreak = myStreak + 1
            else:
                if longest < myStreak:
                    longest = myStreak
                myStreak = 1
        return longest




myobjectx = Solution()
list1= [49, 29, 6, 30, 13, 8, 44, 33, 10, 38, 31, 32]
print myobjectx.longestConsecutive(list1)
