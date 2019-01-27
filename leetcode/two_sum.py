class Solution(object):
    def twoSum(self, myList,target):
        origList = list(myList)
        #for j in range(1,len(myList)):
        #    for k in range(0,len(myList)-1):
        #        if myList[j] < myList[k]:
        #            temp = myList[j]
        #            myList[j] = myList[k]
        #            myList[k] = temp
        excludeElementJ = []
        excludeElementK = []
        foundPair = []
        finalPair = []
        for j in range(0,len(myList)-1):
            if len(foundPair) > 0:
                break
            for k in range(1,len(myList)):
                #if (myList[j] < target) and (myList[k] < target):
                if j != k:
                    sum = int(myList[j]) + int(myList[k])
                    if sum  == int(target):
                        foundPair.append(myList[j])
                        foundPair.append(myList[k])
                        break
        if  len(foundPair) == 2:
            if  foundPair[0] == foundPair[1]:
                p1 = [i for i, n in enumerate(origList) if n == foundPair[0]][0]
                p2 = [i for i, n in enumerate(origList) if n == foundPair[0]][1]
                finalPair.append(p1)
                finalPair.append(p2)
            else:
                p1 = origList.index(foundPair[0])
                p2 = origList.index(foundPair[1])
                if p1 < p2:
                    finalPair.append(p1)
                    finalPair.append(p2)
                else:
                    finalPair.append(p2)
                    finalPair.append(p1)
            return  finalPair
        else:
            return []

myobjectx = Solution()
list1= [49, 29, 6, 30, 13, 8, 44, 33, 10, 38]
target= 35
print myobjectx.twoSum(list1,target)
list1 = [2,7,11,15]
target = 9
print myobjectx.twoSum(list1,target)
list1 = [3,2,4]
target = 6
print myobjectx.twoSum(list1,target)
list1 = [3,3]
target = 6
print myobjectx.twoSum(list1,target)
list1 = [0,4,3,0]
target = 0
print myobjectx.twoSum(list1,target)
