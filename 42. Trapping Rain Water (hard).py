
# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(n) SC --------

class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        for i in range(len(height)):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            total += min(left_max, right_max) - height[i]
        return total


# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        total = 0

        prefix = [0]*n
        postfix = [0]*n

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        
        postfix[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i])
        
        for i in range(n):
            total += min(prefix[i], postfix[i]) - height[i]
        return total


# SOLUTION 3
# ------------------ O(n) TC ----------- O(1) SC --------


