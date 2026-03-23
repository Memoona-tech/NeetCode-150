# SOLUTION 0
# ------------------ O(nlogn) TC ----------- O(n) SC --------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for c in s:
            freq[ord(c) - ord('a')] += 1
        for c in t:
            freq[ord(c) - ord('a')] -= 1
            if freq[ord(c) - ord('a')] < 0:
                return False
        return True
      

# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {}
        for c in rs:
            freq1[c] = freq1.get(c, 0) + 1

        freq2 = {}
        for c in t:
            freq2[c] = freq2.get(c, 0) + 1

        return freq1 == freq2


# SOLUTION 3
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {}
        for c in rs:
            freq1[c] = freq1.get(c, 0) + 1

        freq2 = {}
        for c in t:
            freq2[c] = freq2.get(c, 0) + 1

        for c in s:
            if freq1[c] == freq2.get(c, 0):      # if freq1.get(c, 0) == freq2.get(c, 0):
                continue
            return False
        return True



