class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case
        if not nums:
            return 0
        
        longest = 0
        sequence = set(nums)

        # Looping through array nums
        for i in sequence:
            # Identifying start of sequence
            if i - 1 not in sequence:
                current = i
                length = 1
                # Updating current and length
                while current + 1 in sequence:
                    current += 1
                    length += 1
                
                longest = max(longest,length)
        return longest
            