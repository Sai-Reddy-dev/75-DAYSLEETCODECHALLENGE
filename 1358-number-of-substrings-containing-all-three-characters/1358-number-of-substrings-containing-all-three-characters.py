class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        mp = {}
        for i,c  in enumerate(s):
            mp[c] = i
            if len(mp) < 3:
                continue
            res += min(mp.values()) + 1
        
        return res