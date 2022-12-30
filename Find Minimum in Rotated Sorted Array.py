class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = 5001
        for i in range(len(nums)):
            mini = min(nums[i], mini)

        return mini