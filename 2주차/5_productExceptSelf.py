def productExceptSelf( nums: list) -> list:
    #nums=[1,2,3,4]
    out=[]
    p=1
    for i in range(0,len(nums)):
        out.append(p)
        p=p*nums[i]
        #out=[1,1,2,6]
    p=1
    for i in range(len(nums)-1,-1,-1):#i=3,2,1,0
        out[i]=out[i]*p
        p=p*nums[i]#nums[i]=4,3,2,1
    return out


# input=[a,b,c,d] 이면 output=[ b*c*d , a*c*d , a*b*d , a*b*c ]이다. 
#포함된 인자들을 보면 index 2,3,4에 차례로 a, ab,abc가 곱해짐을 알 수 있다. 
# 그것을 제외하면 뒤에서 차례로 d,cd,bcd가 곱해짐을 알 수 있다. 


            

nums=[1,2,3,4]
print(productExceptSelf(nums))

#배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 
#되도록 출력하라
#O(n)을 만족해야함