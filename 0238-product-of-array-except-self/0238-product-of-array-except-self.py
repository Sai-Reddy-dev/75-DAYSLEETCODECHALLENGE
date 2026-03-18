class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        pro = 1

        for num in nums:
            res.append(pro)
            pro *= num
        
        pro = 1
        for i in range(n-1,-1,-1):
            res[i] *= pro
            pro *= nums[i]
        
        return res
        

