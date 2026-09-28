class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                start_num = num
                length = 1

                while start_num + length in numSet:
                    length += 1

                longest = max(longest, length)
        
        return longest

                    


