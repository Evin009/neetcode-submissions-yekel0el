class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        rows = len(matrix) # 3
        cols = len(matrix[0]) # [1,2,4,8] len = 4

        # convert 2d matrix to 1d array 
        l = 0 
        r = rows * cols - 1 # gives position of last element

        while l <= r:
            mid = (l + r) // 2 # mid idx val in 1d array

            # converting 1d value to 2d val
            row = mid // cols
            col =  mid % cols

            val = matrix[row][col]

            if val == target:
                return True
            
            elif val > target:
                # val in left side
                r = mid - 1
            else:
                l = mid + 1
        
        return False



