class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        last_seen = {}
        max_length = 0

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)
            last_seen[s[r]] = r
            length = r - l + 1
            max_length = max(max_length, length)

        return max_length


