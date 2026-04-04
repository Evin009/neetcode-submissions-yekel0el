class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) - 1
        
        res = []
        while left < right:
            b = right  - left
            l = min(height[left], height[right])
            area = l * b
            res.append(area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max(res)