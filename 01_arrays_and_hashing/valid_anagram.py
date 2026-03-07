class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_count = {}
        for s_char in s:
            s_count[s_char] = s_count.get(s_char, 0) + 1

        for t_char in t:
            if t_char in s_count and s_count[t_char] > 0:
                s_count[t_char] = s_count[t_char] - 1
            else:
                return False
        
        return True
# Time complexity: O(n) where n is the length of the strings
# Space complexity: O(1) since the size of the hash map is limited by the number of characters in the alphabet (assuming ASCII)
