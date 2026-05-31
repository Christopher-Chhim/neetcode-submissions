class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0              # next position for 0
        curr = 0            # current element
        p2 = len(nums) - 1  # next position for 2

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                # do NOT increment curr here, need to check swapped value
            else:  # nums[curr] == 1
                curr += 1