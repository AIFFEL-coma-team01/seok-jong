# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# ex) 
# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [4,1,2,1,2]
# Output: 4

# Input: nums = [1]
# Output: 1





#[CODE]
class Solution:
    def singleNumber(self, nums):
        result=0
        for i in nums:
            result ^= i 
        return result

nums=[4,1,2,1,2]
a=Solution()
print(a.singleNumber(nums))