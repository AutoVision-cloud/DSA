from __future__ import annotations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time complexity: O(N^2), Space complexity: O(1) without output
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]

    print("All tests passed.")
