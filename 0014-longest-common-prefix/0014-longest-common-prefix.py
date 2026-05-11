class Solution:
    def longestCommonPrefix(self, strs):
        v = sorted(strs)
        frist = v[0]
        last = v[-1]
        ans = ''
        for i in range(min(len(frist),len(last))):
            if frist[i] != last[i]:
                return ans 
            ans += frist[i]
        return ans