class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}

        for i in s:
            m[i] = 1 + m.get(i, 0)
        
        for i in t:
            if m.get(i) is None:
                return False
            m[i] -= 1
        
        for _,v in m.items():
            if v != 0:
                return False
        
        return True

        