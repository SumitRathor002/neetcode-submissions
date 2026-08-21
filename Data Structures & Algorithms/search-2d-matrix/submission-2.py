class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_index(num):
            i = num // cols
            j = num % cols
            return i , j

        l = 0 
        rows = len(matrix)
        cols = len(matrix[0])
        r = (rows * cols) - 1
        while l <= r:
            mid = (l + r) // 2
            i, j = get_index(mid)
            print(l, r, mid, i, j)
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return False