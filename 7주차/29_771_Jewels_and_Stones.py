class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in jewels:
            for j in stones:
                if i==j:
                    count+=1

        return count

'''
Runtime: 32 ms, faster than 63.11% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.2 MB, less than 76.02% of Python3 online submissions for Jewels and Stones.
'''


#풀이 1 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        for i in stones:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count=0
        for i in jewels:
            count+=dic[i]

        return count


#풀이 2 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs=collections.defaultdict(int)
        count=0

        for char in stones:
            freqs[char]+=1

        for char in jewels:
            count +=freqs[char]

        return count

'''
Runtime: 32 ms, faster than 63.11% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.9 MB, less than 98.69% of Python3 online submissions for Jewels and Stones.
'''