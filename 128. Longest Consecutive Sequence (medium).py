# SOLUTION 1
# ------------------ O(n log n) TC ----------- O(n) SC --------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # [0,3,7,2,5,8,4,6,0,1] = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

        # [1, 2, 3, 4, 100, 200]

        # [1, 2, 6, 7, 8]

        nums.sort()
        streak = []
        c = current_streak = 1

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                current_streak += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                streak.append(current_streak)
                current_streak = 1
                c = max(streak)
        return max(c, current_streak)


# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:          # it's a start
                current = 0
                while num in num_set:       # keep counting
                    current += 1
                    num += 1
                longest = max(longest, current)

        return longest
