class Solution(object):
    def possible(self,arr,D,m,k):
        cnt = 0
        nf_B = 0

        for i in range(len(arr)):
            if arr[i] <= D:
                cnt += 1
                if cnt == k:
                    nf_B += 1 
                    cnt = 0
            else:
                cnt = 0
        
        return nf_B >= m
        
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)

        if n < (m*k):
            return -1
        
        low , high = min(bloomDay),max(bloomDay)
        ans = high

        while(low <= high):
            mid = (low + high) // 2

            if self.possible(bloomDay,mid,m,k):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans
        