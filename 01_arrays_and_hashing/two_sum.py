from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in my_dict:
                return idx, my_dict[complement]
            my_dict[num] = idx
# Time complexity: O(n)
# Space complexity: O(n)
