class Solution(object):
    def reverse(self,arr,start,end):
        while start < end:
            arr[start] , arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
        
    def rotate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(arr)

        if n == 0:
            return
        
        k %= n

        self.reverse(arr,0,n-1)
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)
        

