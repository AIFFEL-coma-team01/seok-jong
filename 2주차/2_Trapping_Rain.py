def trap( height: list) -> int:
    trap=0
    max_height=max(height)
    height_right=height[height.index(max_height)+1:]
    height_left=height[:height.index(max_height)]
    print(height_left)
    print(height_right)
    def research_right(height_right,max_height):
        print(len(height_right))
        if len(height_right)==1:
            return

        trap=height_right.index(max(height_right))*max(height_right)
        print(trap)
        max_height=max(height_right)
        height_right=height_right[height_right.index(max(height_right))+1:]
        print(height_right)
        #research_right(height_right,max_height)
        
    research_right(height_right,max_height)
    research_right([1,2,1],2)
        


        

        

height=[0,1,0,2,1,0,1,3,2,1,2,1]

trap(height)