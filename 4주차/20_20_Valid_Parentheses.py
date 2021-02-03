'''
LeetCode 20

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.

-------------------------------------------------------------------------------------------------------------------------

1. 반으로 나눠서 중간부터 검사-> {[()]()}의 경우 오류 
2. stack이용해서 close 괄호가 나오면 pop하고 open 괄호가 나오면 stack에 append -> pop했으로 경우 비교해야함 -- dictionary이용 

<pseudo-code>

def isValid(s):
    dic={} -> 비교를 위한 지표 생성
    close=[] -> 닫는 괄호를 검사하기 위한 지표 생성 
    l1=[] -> stack으로 이용할 빈 리스트 생성 
    for s의 길이만큼 반복:
        if 닫는괄호인지 검사:
            맞으면 l1.pop
            if l1.pop==dic[]비교
                맞으면 continue
            else:
                return False
    return True-> 끝까지 모두 수행될 경우 True반환 

'''






class Solution:
    def isValid(self, s: str) -> bool:
        
        dic={')':'(',']':'[','}':'{'}
        close = [')','}',']']
        l1=[] #stack
        for i in s:
            if i not in close: #close 괄호인지 검사
                l1.append(i)
            else:
                if len(l1)==0: #stack에서 꺼낼것이 없으면 False 반환 
                    return False
                else:
                    tmp=l1.pop()
                if tmp==dic[i]:
                    continue
                else:
                    return False
        
        if len(l1)!=0:
            return False #stack안에 data가 없으면 True 남아있으면 False 
        else:
            return True


'''
s=Solution()
input="["
print(s.isValid(input))
'''



'''
<Submissions>

Runtime: 28 ms, faster than 85.01% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 66.76% of Python3 online submissions for Valid Parentheses.
'''