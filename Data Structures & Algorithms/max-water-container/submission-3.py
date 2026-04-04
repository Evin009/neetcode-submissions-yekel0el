class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) - 1
        res = []
        while left < right:
            b = right - left
            l = min(height[right], height[left])
            area = l*b
            res.append(area)
        
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max(res)