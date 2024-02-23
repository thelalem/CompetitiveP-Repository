class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        n,m = len(matrix),len(matrix[0])
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(matrix[j][i])
            transpose.append(arr)
        return(transpose)
                
