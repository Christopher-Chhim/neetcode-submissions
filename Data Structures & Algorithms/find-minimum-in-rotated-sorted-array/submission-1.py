class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # left pointer starts at beginning of array
        left = 0
        
        # right pointer starts at end of array
        right = len(nums) - 1

        # we shrink the search space until only one element remains
        while left < right:
            
            # find the middle index
            middle = (left + right) // 2

            # Case 1: middle value is greater than right value
            if nums[middle] > nums[right]:
                
                # This means middle is in the LEFT (big numbers) portion
                # So the minimum must be somewhere to the RIGHT of middle
                # We eliminate left half including middle
                left = middle + 1

            # Case 2: middle value is less than or equal to right value
            else:
                
                # This means middle is in the RIGHT (small numbers) portion
                # The minimum could be at middle OR to the left of it
                # So we keep middle and eliminate everything to the right
                right = middle

        # When loop ends, left == right
        # That index must be the smallest element
        return nums[left]
