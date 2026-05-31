class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for i in range(len(nums)):
            current_number= nums[i]
            complement = target - current_number

            if complement in seen_numbers:
                return [seen_numbers[complement], i]
            else:
                seen_numbers[current_number] = i
        return None
