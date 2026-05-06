class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in mp:
                return [mp[complement],i]
            
            mp[num] = i

        return [-1,-1]