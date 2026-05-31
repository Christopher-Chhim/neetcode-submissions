class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers
        i = 0
        j = len(heights) - 1

        # Initialize max_area
        max_area = 0

        # Loop
        while i < j:
            # width
            width = j - i
            # area
            area = width * min(heights[i], heights[j])
            # update max_area
            max_area = max(max_area, area)
            if heights[i] < heights[j]:
                # increment left pointer
                i += 1
            else:
                # decrement right pointer
                j -= 1
        return max_area

        