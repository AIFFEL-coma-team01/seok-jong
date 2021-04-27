# 461. Hamming Distance

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

# ex) 
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.


# Input: x = 3, y = 1
# Output: 1



# [CODE]

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=bin(x^y)
        return result.count("1")

a= Solution()
x=3
y=1
print(a.hammingDistance(x,y))