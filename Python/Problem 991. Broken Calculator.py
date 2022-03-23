class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while startValue < target:
            res += target % 2 + 1
            target = (target + 1) // 2
        return res + startValue - target