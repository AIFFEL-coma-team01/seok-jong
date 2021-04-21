# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


# EX)

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false


#CODE

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j==target:
                    return True
                elif j>target:
                    break
        return False


# RESULT

# Runtime: 168 ms, faster than 47.42% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.6 MB, less than 28.39% of Python3 online submissions for Search a 2D Matrix II.
