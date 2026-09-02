class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows-1][columns-1]:
            return False
        top, bot = 0, rows-1
        target_row = False
        while top <= bot:
            mid = top + (bot-top)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][columns-1] < target:
                top = mid+1
            elif matrix[mid][0] > target:
                bot = mid-1
            else:
                target_row = matrix[mid]
                break
        if not target_row:
            return False
        l, r = 0, columns-1
        while l <= r:
            mid = l + (r-l)//2
            if target_row[mid] < target:
                l = mid+1
            elif target_row[mid] > target:
                r = mid-1
            else:
                return True
        return False