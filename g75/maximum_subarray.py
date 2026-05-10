from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time complexity: O(N), Space complexity: O(1)
        current_sum = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_so_far = max(max_so_far, current_sum)

        return max_so_far


if __name__ == "__main__":
    s = Solution()

    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([-1, -2, -3]) == -1

    print("All tests passed.")
