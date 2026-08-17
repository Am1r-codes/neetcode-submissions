class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(char.lower() for char in s if char.isalnum())

        l = 0
        r = len(stripped) - 1
        while l < r:
            if stripped[l] != stripped[r]:
                return False
            l += 1
            r -= 1
        return True