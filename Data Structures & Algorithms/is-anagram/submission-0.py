class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for char in s:
            if char not in hash1:
                hash1[char] = 1
            else:
                hash1[char] += 1
        for char in t:
            if char not in hash2:
                hash2[char] = 1
            else:
                hash2[char] += 1
        if len(hash1) != len(hash2):
            return False
        for char in hash1:
            if char not in hash2:
                return False
            if hash1[char] != hash2[char]:
                return False
        return True