def maxProfit( prices:list) -> int:
    tmp=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            tmp=max(tmp,prices[j]-prices[i])
   
    
    return tmp
            


prices=[7,1,5,3,6,4]
print(maxProfit(prices))

#한번의 거래로 낼 수 있는 최대 이익을 산출하라.
#단순히 이득의 크기만 구하면 됨에 집중 