#https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedList = sorted(nums)
        doubles = []
        
        for i in range(len(sortedList)-1):
            if sortedList[i] == sortedList[i+1]:
                doubles.append(sortedList[i])
        
        return doubles
                
                            
