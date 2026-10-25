class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0 
        max_length = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            rep = (r - l + 1) - max(count.values())
            while rep > k:
                count[s[l]] -= 1
                l += 1
                rep =  (r - l + 1) - max(count.values())
            max_length = max(max_length, r - l + 1)
        
        return max_length
