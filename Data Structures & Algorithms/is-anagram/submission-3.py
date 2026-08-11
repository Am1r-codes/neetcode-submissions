class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = Counter(s)
        t_counts = Counter(t)

        return all(s_counts[char] == t_counts[char] for char in s_counts)