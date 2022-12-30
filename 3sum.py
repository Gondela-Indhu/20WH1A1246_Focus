class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if sum(nums) == 0:
                nums.sort()
                return [nums]
            else:
                return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ls = (nums[i], nums[j], nums[k])
                    ans.append(ls)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
                    
        d = list(set(tuple(ans)))
        return d
                        