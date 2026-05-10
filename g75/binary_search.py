from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(log N), Space complexity: O(1)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_idx = left + (right - left) // 2
            if target == nums[mid_idx]:
                return mid_idx
            elif target > nums[mid_idx]:
                left = mid_idx + 1
            else:
                right = mid_idx - 1

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert s.search([5], 5) == 0
    assert s.search([5], 3) == -1

    print("All tests passed.")
