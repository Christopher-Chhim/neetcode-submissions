class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map: key = number, value = its index
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            # If the complement exists, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # Otherwise, store the current number and its index
            num_to_index[num] = i