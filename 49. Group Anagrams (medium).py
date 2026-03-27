# SOLUTION 1
# ------------------ O(n * k log k) TC ----------- O(n * k) SC --------
# Sort each string to create canonical key - most readable
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
            
        return list(res.values())


# SOLUTION 2
# ------------------ O(n * k) TC ----------- O(n * k) SC --------
# Frequency array as hashable key - optimal for lowercase letters
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            res[tuple(freq)].append(s)
            
        return list(res.values())

