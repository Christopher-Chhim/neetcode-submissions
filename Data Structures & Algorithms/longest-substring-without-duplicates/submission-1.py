class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0

        if not s:
            return 0
        
        # make right equal to the end of the char s
        for right in range(len(s)):
            # remove dupe
            while s[right] in seen:
                seen.remove(s[left])
                # shift by 1
                left += 1
            seen.add(s[right])
            # update longest length
            res = max(res, right - left + 1)
        return res