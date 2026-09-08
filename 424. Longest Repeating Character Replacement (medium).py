# SOLUTION 1 BRUTE FORCE
# ------------------ O(N^3) TC ----------- O(26) SC --------


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            
            for j in range(i, n):
                substring = s[i:j+1]

                freq = {}
                for char in substring:
                    freq[char] = freq.get(char, 0) + 1

                max_freq = max(freq.values()) if freq else 0
            
                if (len(substring) - max_freq) <= k:
                    max_len = max(len(substring), max_len)

        return max_len



# SOLUTION 2
# ------------------ O(N) TC ----------- O(1) SC --------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        max_len = 0
        max_freq = 0
        freq = {}

        for r in range(len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1
            
            max_freq = max(freq.values()) if freq else 0

            while ((r-l+1) - max_freq) > k:
                freq[s[l]] = freq.get(s[l]) - 1

                # Also, freq.get(s[l]) - 1 will crash if s[l] is not in freq. Better:
                
                # freq[s[l]] -= 1
                # if freq[s[l]] == 0:
                    # del freq[s[l]]
                # l += 1
                l += 1
            
            max_len = max(max_len, r-l+1)

        return max_len
