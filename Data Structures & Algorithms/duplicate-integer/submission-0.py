class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums:
            if m.get(i) is not None:
                return True
            m[i] = 0
        return False