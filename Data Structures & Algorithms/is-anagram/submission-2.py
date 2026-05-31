class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case
        if len(s) != len(t):
            return False

        # Initiating a dictionary to store unique values and their relative frequencies
        count_s = {}

        # Looping through s to create the hash map and store each unique value and their relative frequencies.
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
        
        # Loop through t and compare it with count_s
        for i in t:
            if i not in count_s:
                return False 
            count_s[i] -= 1
            if count_s[i] < 0:
                return False
        return True


        
        

        