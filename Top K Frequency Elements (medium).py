# SOLUTION 1
# ------------------ O(n log n) TC ----------- O( len(nums) ) SC --------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = list(freq.keys())
        res.sort(key = lambda x: freq[x], reverse = True)
        return res[:k]

# SOLUTION 2
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(num)+1)]

        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        for i in range(len(buckets), 0, -1):
            for num in bucket[i]:
              res.append(num)
              if len(res) == k:
                  return res
        return res
        
