class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = [0] * 26
        for char in s:
            s_char[ord(char) - ord('a')] += 1
        t_char = [0] * 26
        for char in t:
            t_char[ord(char) - ord('a')] += 1
        if s_char == t_char:
            return True
        # if sorted(s) == sorted(t):
        #     return True
        return False