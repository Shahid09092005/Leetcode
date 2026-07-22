class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rSet= set()
        cSet = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if(matrix[i][j]==0):
                    rSet.add(i)
                    cSet.add(j)
            # ourt of inner loop
        # out of outer loop
        # convert rows to zeros
        for r in rSet:
            for j in range(0,cols):
                matrix[r][j]=0
        # convert cols to zeros
        for c in cSet:
            for i in range(0,rows):
                matrix[i][c]=0
        # return modify matrix
        return matrix
        