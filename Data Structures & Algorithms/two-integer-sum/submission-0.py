class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumComp = {}
        for index, item in enumerate(nums):
            if sumComp.get(target - item) is not None:
                return [ sumComp[target-item], index]
            sumComp[item] = index
        return []
        