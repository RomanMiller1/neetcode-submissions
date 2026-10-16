class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            current = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > current:
                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = h * width
                max_area = max(area, max_area)

            if i < n:
                stack.append(i)

        return max_area
    





