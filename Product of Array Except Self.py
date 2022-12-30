class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]

        count = nums.count(0)
        if count == 0:
            for i in nums:
                ans = product // i
                lst.append(ans)
        elif count == 1:
            for i in nums:
                if i == 0:
                    lst.append(product)
                else:
                    lst.append(0)
        else:
            for i in nums:
                lst.append(0)

        return lst
