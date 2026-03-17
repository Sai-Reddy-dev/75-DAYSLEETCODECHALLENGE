class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]

        for key in freq_map:
            freq = freq_map[key]
            bucket[freq].append(key)
        
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for val in bucket[i]:
                    res.append(val)
                    if len(res) == k:
                        return res
        
        return res
        