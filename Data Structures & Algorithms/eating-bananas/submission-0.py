class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       # start at 1, because that's the minimum possible speed
       left = 1
       # greatest possible speed
       right = max(piles)

       # loop until the left and right pointers cross
       while left <= right:
        # keep track of hours
            hours = 0
            k = (left + right) // 2
            # loop through every pile in piles
            for pile in piles:
                # hours is equal to the ??
                hours += (pile + k - 1) // k
            if hours <= h:
                # shift right pointer to middle index - 1 because it means that k is too fast.
                right = k - 1
            else:
                # shift left pointer to middle index + 1 because it means that k is too slow.
                left = k + 1
       return left
                    
