class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize two pointers
        i = 0
        j = len(heights) - 1

        max_area = 0

        # loop through the pointers
        while i < j:
            width = j - i
            area = width * min(heights[i], heights[j])
            max_area = max(max_area, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area