class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [sum(nums[:i+1]) for i in range(len(nums))]
        return ans
