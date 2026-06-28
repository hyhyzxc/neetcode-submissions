class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        rowArr = list(matrix[i][-1] for i in range(rows))

        l, r = 0, len(rowArr) - 1

        while l <= r:
            mid = (l + r) // 2
            if target <= rowArr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        if l >= len(rowArr):
            return False
            
        colArr = matrix[l]

        l, r = 0, len(colArr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if colArr[mid] == target:
                return True
            elif colArr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        