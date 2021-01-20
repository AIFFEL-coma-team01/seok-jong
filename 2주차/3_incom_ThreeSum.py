
def threeSum(nums: list) -> list:
    result=[]
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i] ==nums[i-1]:
            continue
            
            

nums=[-1,0,1,2,-1,-4]

print(threeSum(nums))

