class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Schars: dict[str, int] = {}
        Tchars: dict[str, int] = {}

        for char in s:
            Schars[char] = Schars.get(char, 0) + 1

        for char in t:
            Tchars[char] = Tchars.get(char, 0) + 1

        return Schars == Tchars
