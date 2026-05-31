class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        # looping through 
        while top <= bottom:
            row = (top + bottom) // 2
            # checks to see if target is greater than greatest number in the row
            if target > matrix[row][-1]:
                top = row + 1
            # checks to see if target is less than greatest number in the previous row
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
            # conditional statement if target is within the row
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        left = 0
        right = columns - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
        