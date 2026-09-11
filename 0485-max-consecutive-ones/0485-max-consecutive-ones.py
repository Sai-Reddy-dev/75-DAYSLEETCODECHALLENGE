class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        n = len(nums)

        for i in  nums:
            if i:
                count += 1
            else:
                if max_count < count:
                   max_count = count
                count = 0
        if max_count < count:
            max_count = count
            count = 0
        return max_count
