class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1 : Transform
        rows=len(matrix)
        cols=len(matrix[0])
        for r in range(0,rows):
            for c in range(r,cols):
                if(r!=c):
                    # swap i,j to j,i
                    temp = matrix[r][c]
                    matrix[r][c]=matrix[c][r]
                    matrix[c][r]=temp
        # now swap cols
        for r in range(0,rows):
            st = 0
            ed = cols-1
            while(st<ed):
                temp = matrix[r][st]
                matrix[r][st] = matrix[r][ed]
                matrix[r][ed]=temp
                st+=1
                ed-=1
        return matrix
        