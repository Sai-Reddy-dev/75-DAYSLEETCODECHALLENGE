class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0
        
        st = set()
        largest = 1

        for i in range(n):
            st.add(nums[i])
        
        for it in st:
            if it - 1 not in st:
                cnt = 1
                x = it
            
                while x+1 in st:
                    x = x + 1
                    cnt += 1
                largest = max(largest,cnt)

        return largest
        

        