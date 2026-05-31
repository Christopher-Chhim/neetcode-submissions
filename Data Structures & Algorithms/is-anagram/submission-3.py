class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # Edge case
        if len(s) != len(t):
            return False
    
        #initialize the count
        count_s = {}

        #creating hashmap for s
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
    
        #compare t hashmap to s
        for i in t:
            if i not in count_s:
                return False

            count_s[i] -= 1
            if count_s[i] < 0:
                return False
        return True


        
        

        