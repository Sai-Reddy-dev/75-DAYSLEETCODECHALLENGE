class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n == 0:
            return
        
        k = k % n

        nums[n-k:] = reversed(nums[n-k:])

        nums[:n-k] = reversed(nums[:n-k])

        nums[:] = reversed(nums)
            

