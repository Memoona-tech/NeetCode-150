# SOLUTION 1
# ------------------ O(n²) TC ----------- O(1) SC --------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1

        i = 0
        while i < len(nums):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    prod *= nums[j]
            res.append(prod)
            prod = 1
            i += 1
        return res


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
