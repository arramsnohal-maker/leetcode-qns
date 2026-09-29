class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        first=0
        last=m*n-1
        while first<=last:
            mid=(first+last)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                first=mid+1
            else:
                last=mid-1
        return False