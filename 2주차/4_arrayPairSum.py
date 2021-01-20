def arrayPairSum( nums: list) -> int:
    nums.sort()
    iter=int(len(nums)/2)
    tmp=0
    for i in range(iter):
        n2=nums.pop()
        n1=nums.pop()
        tmp+=min(n1,n2)
    return tmp


    
nums=[1,4,3,2]
print(arrayPairSum(nums))

#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
#sort를 이용하여 배열을 오름차순으로 재배열한 후에 순서대로 페어링 
