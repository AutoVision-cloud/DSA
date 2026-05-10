class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity is O(N), space complexity is O(1)
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == "__main__":
    s = Solution()

    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    assert s.isPalindrome("0P") == False

    print("All tests passed.")
