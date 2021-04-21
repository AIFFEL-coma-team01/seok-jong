# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# ex)
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.



#CODE

class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1)&set(nums2)



# RESULT

# Runtime: 40 ms, faster than 90.67% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.3 MB, less than 90.39% of Python3 online submissions for Intersection of Two Arrays.



#책 코드 
class Solution:
    def intersection(self, nums1, nums2):
        result:Set=set()
        
        #양쪽 모두 정렬 
        nums1.sort()
        nums2.sort()
        i=j=0
        
        # 투 포인터 우측으로 이동하며 일치 여부 판별 
        while i<len(nums1) and j <len(nums2):
            if nums1[i] >nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                result.add(nums1[i])
                i+=1
                j+=1

        return result

nums1=[1,2,2,1]
nums2=[2,2]
a=Solution()
print(a.intersection(nums1,nums2))