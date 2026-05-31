class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Count characters in s
            if char_s in count_s:
                count_s[char_s] += 1
            else:
                count_s[char_s] = 1
        
            if char_t in count_t:
                count_t[char_t] += 1
            else:
                count_t[char_t] = 1
        
        return count_s == count_t