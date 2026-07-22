class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = cols-1
        top = 0
        bottom = rows-1
        n=0
        totalEle=rows*cols
        ans=[]
        while(n<totalEle):
            # move left to right and then increase top
            for i in range(left,right+1):
                if(n<totalEle):
                    ans.append(matrix[top][i])
                    # print(matrix[top][i])
                n+=1
            top+=1
            # move right to bottom and then decrease right
            for i in range(top,bottom+1):
                if(n<totalEle):
                    ans.append(matrix[i][right])
                    # print(matrix[i][right])
                n+=1
            right-=1
            # move right to left
            tempr=right
            while(n<totalEle and tempr>=left):
                ans.append(matrix[bottom][tempr])
                # print(matrix[bottom][tempr])
                n+=1
                tempr-=1
            bottom-=1
            #move bottom to top
            tempb=bottom
            while(n<totalEle and tempb>=top):
                ans.append(matrix[tempb][left])
                # print(matrix[tempb][left])
                tempb-=1
                n+=1
            left+=1
        # ends main while loop
        return ans