class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, right = 0, len(matrix[0])
        left, bottom = 0, len(matrix)

        res = []

        rows = len(matrix)
        cols = len(matrix[0])

        while top < bottom and left < right:
            # add all top elements
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if len(res) == rows * cols:
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
            
            
        
        return res
            