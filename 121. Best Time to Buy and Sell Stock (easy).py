
# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit


# SOLUTION 2       (Two Pointers (Sliding Window)
# ------------------ O(n) TC ----------- O(1) SC --------

# IF THE DIFFERENCE IS INCREASING BY FUTURE THAT SILENTLY IMPLIES THAT FUTURE VALUES ARE BIGGER (THAT'S WHY THEY'RE GIVING LARGER DIFFERENCE) SO IT'S NOT REGRETFULFUL TO SKIP THE CURRENT LEFT_POINTER VALUE IN THE OTHERWISE CASE (THE ELSE CASE FROM THIS INCREASING_DIFFERNCE ONE)
# ALSO THE 'IF' CONDITION IS CHECKING THIS EXACT THING IN REAL ! THAT IF FUTURE VALUE IS BIGGER THAT THIS LEFT POINTER, RIGHT...? OTHERWISE WE'LL JUST GO WITH THE L = R ONE.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # buy pointer
        right = 1  # sell pointer
        max_profit = 0
        
        while right < len(prices):
            # If profitable, calculate profit
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # If not profitable, move buy pointer to current position
                left = right
            right += 1
        
        return max_profit



# SOLUTION           (Kadane's Algorithm (Maximum Subarray)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # buy pointer
        right = 1  # sell pointer
        max_profit = 0
        
        while right < len(prices):
            # If profitable, calculate profit
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # If not profitable, move buy pointer to current position
                left = right
            right += 1
        
        return max_profit



# SOLUTION 3         (Dynamic Programming (States))
# ------------------ O(n) TC ----------- O(1) SC --------

  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # dp[i][0] = max profit on day i without holding stock
        # dp[i][1] = max profit on day i holding stock
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0  # no stock, no profit
        dp[0][1] = -prices[0]  # bought stock, spent money
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])  # can only buy once
        
        return dp[-1][0]  # max profit without holding stock



# SOLUTION 4         (DP with Space Optimization)
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Only need previous day's states
        not_hold = 0  # max profit without stock
        hold = -prices[0]  # max profit with stock (bought)
        
        for price in prices[1:]:
            new_not_hold = max(not_hold, hold + price)
            new_hold = max(hold, -price)
            not_hold, hold = new_not_hold, new_hold
        
        return not_hold
