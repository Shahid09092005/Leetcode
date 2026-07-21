class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows =len(grid)
        cols = len(grid[0])
        n = rows*cols
        k=k%n
        # reverse whole as we do i n 1D
        def reverse(st,ed,cols):
            while(st<ed):
                r1 = st//cols
                c1 = st%cols
                # end
                r2=ed//cols
                c2=ed%cols
                temp = grid[r1][c1]
                grid[r1][c1]=grid[r2][c2]
                grid[r2][c2]=temp
                st+=1
                ed-=1
        reverse(0,n-1,cols)
        reverse(0,k-1,cols)
        reverse(k,n-1,cols)
        return grid
                
        