# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# ex)
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Input: nums = [1], target = 0
# Output: -1


#code 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


# result

# Runtime: 40 ms, faster than 69.81% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.5 MB, less than 79.49% of Python3 online submissions for Search in Rotated Sorted Array.
