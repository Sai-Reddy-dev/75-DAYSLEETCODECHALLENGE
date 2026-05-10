class Solution(object):
    def maxElement(self,arr,col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = max(arr[i][col],max_val)
                index = i
        return index
        
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high) // 2
            row = self.maxElement(mat,mid)
            left = mat[row][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid+1 < n else float('-inf')

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif mat[row][mid] < left:
                high = mid -1
            else:
                low = mid+1

        return [-1,-1]


        