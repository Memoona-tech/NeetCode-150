# SOLUTION 0
# ------------------ O(n) TC ----------- O(min(n,26)) SC --------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Store character → its latest index
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len



# SOLUTION 1
# ------------------ O(n) TC -----------O(min(n,m)) SC --------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        max_len = 0

        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                max_len = max(max_len, r-l+1)

            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            

        return max_len  

                                                                          OR

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                max_len = max(max_len, r-l+1)

            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            r += 1

        return max_len  

            

# SOLUTION 2
# ------------------ O(n) TC ----------- O(min(n,m)) SC --------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = {}
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            r += 1

        return max_len  

            

