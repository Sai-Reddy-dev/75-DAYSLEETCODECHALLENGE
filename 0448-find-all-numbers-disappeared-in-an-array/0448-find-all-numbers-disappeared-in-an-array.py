class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = set(nums)
        nums2 = set(range(1,n+1))
        return list(nums2 - nums)

        