from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solution using sorting
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False
# Time complexity: O(n log n) due to sorting
# Space complexity: O(1) if we ignore the space used by sorting, otherwise O