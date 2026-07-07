# SOLUTION 1
# ------------------ O(N^2) TC ----------- O(1) SC --------

class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0

        for l in range(len(height)-1):
            r = l+1

            while r < len(height):
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)
                r += 1
        
        return res  




# SOLUTION 2 

----- OPTIMIZED ---------
# ------------------ O(N) TC ----------- O(1) SC --------

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height)-1
        res = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return res
