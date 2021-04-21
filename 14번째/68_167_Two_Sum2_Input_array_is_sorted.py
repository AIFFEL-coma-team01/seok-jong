# 167. Two Sum II - Input array is sorted(#실패)

# Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# ex)

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Input: numbers = [-1,0], target = -1
# Output: [1,2]


#CODE(책 풀이)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        
        while not left==right:
            if numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                return left+1,right+1


# RESULT
# Runtime: 60 ms, faster than 82.44% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.8 MB, less than 5.77% of Python3 online submissions for Two Sum II - Input array is sorted.

#책 코드 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k,v in enumerate(numbers):
            expected = target-v
            i = bisect.bisect_left(numbers[k+1:],expected)
            if i< len(numbers[k+1:]) and numbers[i+k+1]==expected:
                return k+1,i+k+2

                