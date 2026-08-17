class Solution:
    def isPalindrome(self, s: str) -> bool:
        _stripped = "".join(char.lower() for char in s if char.isalnum())

        l = 0
        r = len(_stripped) - 1
        while l < r:
            if _stripped[l] != _stripped[r]:
                return False
            l += 1
            r -= 1
        return True