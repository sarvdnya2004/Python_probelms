class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0)+1
        
        l = dict.keys()
        return list(l)
    
s = Solution()
nums = [1,2,3,1,2,4]
l = s.removeDuplicates(nums)
print(l)