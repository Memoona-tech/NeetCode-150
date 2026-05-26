# SOLUTION 1
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        st = re.sub(r'[^a-zA-Z0-9]', '', s)

        rv = st[::-1]

        return st == rv


# SOLUTION 2
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1

        return True
        
