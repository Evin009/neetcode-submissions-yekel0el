class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # breath = max difference
        # height = min differenct
        res = []
        left, right = 0, len(heights) - 1
        while left < right:
            b = right - left
            l = min(heights[left], heights[right])
            area = l * b

            res.append(area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max(res)

            