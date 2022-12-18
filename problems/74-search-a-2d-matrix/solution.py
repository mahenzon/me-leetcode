class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            # middle_row = bottom + (bottom - top) // 2
            middle_row_idx = (top + bottom) // 2

            row = matrix[middle_row_idx]
            if target > row[-1]:
                top = middle_row_idx + 1
            elif target < row[0]:
                bottom = middle_row_idx - 1
            else:
                break
        else:
            return False

        left = 0
        right = len(row)

        while left <= right:
            # middle = left + (right - left) // 2
            middle = (left + right) // 2

            value = row[middle]
            if value == target:
                return True

            if target > value:
                left = middle + 1
            else:
                right = middle - 1

        return False


