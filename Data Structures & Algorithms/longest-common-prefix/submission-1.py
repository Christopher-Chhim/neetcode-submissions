class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ## Initialize an empty string res to build the common prefix
        res =""

        ## Loop over each index i from 0 to length of the first word in strs:
       
        for i in range(len(strs[0])):
            ## Let char = strs[0][i]   // character at position i in the first string
            char = strs[0][i]

            ## Loop through all the remaining words in the list (strs[1:]):
            for word in strs[1:]:
                ## If i is out of bounds for the current word OR word[i] != char:
                if i >= len(word) or word[i] != char:
                    ## Return the result string res (because mismatch or word too short)
                    return res
            ## Add char to res (since all words matched at index i)
            res += char
        ## Return the final result res
        return res