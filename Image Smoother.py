class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for ni in range(-1,2):
                    for nj in range(-1,2):
                        x,y = i + ni, j + nj
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                result[i][j] = floor(total / count)

        return result
