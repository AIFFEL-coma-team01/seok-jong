# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# ex)
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


#code

class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1

nums=[-1,0,3,5,9,12]
target=2
a=Solution()
print(a.search(nums,target))


# result
# Runtime: 244 ms, faster than 22.70% of Python3 online submissions for Binary Search.
# Memory Usage: 15.6 MB, less than 68.44% of Python3 online submissions for Binary Search.