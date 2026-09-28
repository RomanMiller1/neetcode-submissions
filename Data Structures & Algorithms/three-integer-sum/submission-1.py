class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = - nums[i]
            L = i + 1
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] > target:
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    res.append([nums[L], nums[R], nums[i]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return res        
                

                



        