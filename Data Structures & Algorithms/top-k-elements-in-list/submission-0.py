class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in group:
                group[num] = 1
            else:
                group[num] += 1
        freg = [[] for i in range(len(nums)+1)]
        for num in group:
            count = group[num]
            freg[count].append(num)
        
        res = []
        for i in range(len(freg) - 1, 0, -1):
            for num in freg[i]:
                res.append(num)
                if len(res) == k:
                    return res


        