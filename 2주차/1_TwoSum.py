
def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        print("i; ",i)
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

    



nums=[0,4,3,0]
target=0

print(twoSum(nums,target))


# 덧셈하여 타겟을 만들 수 있는 배열으 두 숫자 인덱스를 리턴 
# 인덱스를 반환한는 것에 주의 
