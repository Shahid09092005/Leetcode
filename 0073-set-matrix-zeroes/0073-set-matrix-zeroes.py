class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstColContainsZero = False
        isFirstRowContainsZero = False
        rows = len(matrix)
        cols = len(matrix[0])
        # checking in first rows
        for c in range(0,cols):
            if(matrix[0][c]==0):
                isFirstRowContainsZero=True
                break
        # checking in first cols
        for r in range(0,rows):
            if(matrix[r][0]==0):
                isFirstColContainsZero=True
                break
        # now using first row and cols for referecne that contains zero
        for r in range(1,rows):
            for c in range(1,cols):
                if(matrix[r][c]==0):
                    # for firstRow
                    matrix[0][c]=0
                    # for firstCol
                    matrix[r][0]=0
        # outter loop ends here
        # matrix 0 modifications
        for r in range(1,rows):
            for c in range(1,cols):
                if(matrix[0][c]==0 or matrix[r][0]==0):
                    matrix[r][c]=0
        # outter loop ends here
        # matrix 0 modifications
        # now changes in first rows
        if(isFirstRowContainsZero):
            for c in range(0,cols):
                matrix[0][c]=0

        # for first cols
        if(isFirstColContainsZero):
            for r in range(0,rows):
                matrix[r][0]=0
        # return ans
        return matrix



