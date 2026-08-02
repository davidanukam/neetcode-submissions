class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(row: int, target: int, front: int, back: int) -> bool:
            if front <= back:
                mid = (front + back) // 2
                if target == matrix[row][mid]:
                    return True
                if target > matrix[row][back]:
                    if row == len(matrix) - 1:
                        return False
                    return binary(row + 1, target, 0, len(matrix[row + 1]) - 1)
                if target > matrix[row][mid]:
                    return binary(row, target, mid + 1, back)
                else:
                    return binary(row, target, front, mid - 1)
            return False
        
        return binary(0, target, 0, len(matrix[0]) - 1)
        