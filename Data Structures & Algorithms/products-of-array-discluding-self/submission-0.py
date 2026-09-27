class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        total = 1

        for i in range(len(nums)):
            left[i] = total
            total *= nums[i]

        right = [1] * len(nums)
        total = 1

        for i in range(len(nums) - 1, -1, - 1):
            right[i] = total
            total *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
