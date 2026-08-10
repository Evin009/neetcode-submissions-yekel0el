class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # only can store water till the height of the lowest pillar
        # farther the pillar more water it can store 

        max_vol = 0
        l, r = 0, len(heights) - 1

        max_vol = 0
        while l < r:
            length = r - l
            vol = length * min(heights[r], heights[l])
            max_vol = max(vol, max_vol)

            # if left > right to get max vol - we need max height possible
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_vol

            
