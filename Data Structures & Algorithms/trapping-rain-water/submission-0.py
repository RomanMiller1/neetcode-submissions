class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        left_max = 0
        right_max = 0
        total_water = 0 

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if height[l] < height[r]:
                water = left_max - height[l]
                l += 1
                total_water += water
            else:
                water = right_max - height[r]
                r -= 1
                total_water += water
        
        return total_water

        