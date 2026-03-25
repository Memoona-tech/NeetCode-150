# SOLUTION 1
# ------------------ O(n^2) TC ----------- O(1) SC --------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if j != i and nums[i] + nums[j] == target:
                        return [i, j]


# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i


# there's one more solution using hashmap-- it does twice pass 
