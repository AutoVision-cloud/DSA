from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time complexity: O(n), Space complexity: O(1)
        low = 0
        high = len(numbers) - 1

        while low < high:
            sum_two_nums = numbers[low] + numbers[high]

            if sum_two_nums == target:
                return [low + 1, high + 1]

            if sum_two_nums > target:
                high -= 1
            else:
                low += 1

        return [-1, -1]


if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
    assert s.twoSum([1, 2, 3, 4, 5], 9) == [4, 5]

    print("All tests passed.")
