# SOLUTION 1
# ------------------ O(N) TC ----------- O(1) SC --------

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def isFreqEqual(freq1, freq2):
            for i in range(26):
                if freq1[i] != freq2[i]:
                    return False
            return True
        freq = [0] * 26
        winFreq = [0] * 26

        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            winFreq[ord(s2[i]) - ord('a')] += 1

        if isFreqEqual(freq, winFreq):
            return True

        for i in range(len(s1), len(s2)):
            winFreq[ord(s2[i]) - ord('a')] += 1
            winFreq[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if isFreqEqual(freq, winFreq):
                return True

        return False
