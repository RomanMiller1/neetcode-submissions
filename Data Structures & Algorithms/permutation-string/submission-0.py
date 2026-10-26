class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        l = 0

        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1

        if len(s1) > len(s2):
            return False

        count_s2 = {}
        for i in range(len(s1)):
            count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1
        
        if count_s1 == count_s2:
            return True

        for r in range(len(s1), len(s2)):
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            
            count_s2[s2[l]] = count_s2.get(s2[l], 0) - 1
            
            if count_s2[s2[l]] == 0:
                count_s2.pop(s2[l])
            l += 1

            if count_s1 == count_s2:
                return True
        
        return False



