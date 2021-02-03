'''
LeetCode 739

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

-------------------------------------------------------------------------------------------------------------------------
1. pointer를 이용한 2중 반복문 풀이 -> Time Limit Exceeded


'''

#1. pointer를 이용한 2중 반목분 풀이

class Solution:
    def dailyTemperatures(self, T):
        l1 =[]
        tmp=0
        present=0
        for i in range(len(T)):
            for j in range(len(T)-i-1):
                r_idx=j+i+1
                print("i :{}, r_index: {}, T[i]: {}, T[r_idx]: {}".format(i,r_idx,T[i],T[r_idx]))
                if T[i]<T[r_idx]:
                    l1.append(r_idx-i)
                    break
                if r_idx==len(T)-1:
                    l1.append(0)   
                    break
        l1.append(0)
        return l1
        






T = [73, 74, 75, 71, 69, 72, 76, 73]
s=Solution()
print(s.dailyTemperatures(T))