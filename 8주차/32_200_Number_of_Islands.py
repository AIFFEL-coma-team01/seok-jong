import copy
class Solution:
    def numIslands(self, grid):

        def row_zero(list,j,coor):
            if j==-1:
                return
            if list[j]=="0":
                return 
            coor.append(j)
            print("뀨 ",coor)
            list[j]="0"
            if j==len(list)-1:
                return
            print(i," ",j)
            
            if list[j+1]=="1":
                print(grid[i])
                row_zero(list,j+1,coor)
            if list[j-1]=="1":
                row_zero(list,j-1,coor)
            col_zero(coor)
            return 

        def col_zero(coor):
            if len(coor)=="0":
                return 
            tmp=copy.deepcopy(coor)
            coor=[]
            for g in tmp:
                row_zero(grid[i+1],g,coor)
            return


        
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    
                    count+=1
                    print("count: ",count)
                    while True:
                        coor=[]
                        row_zero(grid[i],j,coor)
                        if len(coor)==0:
                            break
                        #tmp=copy.deepcopy(tmp)
                        coor=[]
                        col_zero(coor)
                    
        
        return count



a=Solution()
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(a.numIslands(grid))