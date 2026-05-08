class Solution:
    def isValid(self, s: str) -> bool:
        # Time complexity: O(N), Space complexity O(N)
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    s = Solution()

    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([])") == True
    assert s.isValid("]") == False

    print("All tests passed.")
