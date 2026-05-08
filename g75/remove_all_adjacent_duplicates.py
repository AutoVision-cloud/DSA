class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Time complexity: O(N), space complexity: O(N)
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


if __name__ == "__main__":
    s = Solution()

    assert s.removeDuplicates("abbaca") == "ca"
    assert s.removeDuplicates("azxxzy") == "ay"
    assert s.removeDuplicates("aabb") == ""
    assert s.removeDuplicates("abc") == "abc"
    assert s.removeDuplicates("") == ""

    print("All tests passed.")
