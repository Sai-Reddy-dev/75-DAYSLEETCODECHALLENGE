class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum=float('inf')
        n=len(nums)
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                currect_sum = nums[i] + nums[left] + nums[right]
                if abs(currect_sum - target) < abs(closest_sum - target):
                    closest_sum = currect_sum
                if currect_sum < target:
                    left+=1
                elif currect_sum > target:
                    right -=1
                else:
                    return currect_sum
        return closest_sum