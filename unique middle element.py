class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        element = nums[mid]

        if nums.count(element) == 1:
            return True
        else:
            return False
