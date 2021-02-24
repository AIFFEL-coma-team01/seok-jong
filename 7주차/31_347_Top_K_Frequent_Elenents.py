class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.defualtdict(int)
        for i in nums:
            dic[i]+=1

        k_list=[]
        for key,value in dic.items():
            if value>=k:
                k_list.append(key)
        return k_list
