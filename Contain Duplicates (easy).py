# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------
# Making set from an array requires iterating through entire array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return True if len(unique) < len(nums) else False


# SOLUTION 3
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
        return False
