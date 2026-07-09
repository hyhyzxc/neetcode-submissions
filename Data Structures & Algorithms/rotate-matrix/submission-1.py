class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 7 8 9
        # 4 5 6
        # 1 2 3
        matrix.reverse()
        # 0, 1 -> 1, 0
        # 0, 2 -> 2, 0
        # 1, 2 -> 2, 1

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        
        