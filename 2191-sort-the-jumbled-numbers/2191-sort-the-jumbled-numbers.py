class Solution:
    def convert(self, mapping: List[int], num: int) -> int:
        if num < 10:
            return mapping[num]
        x = num // 10
        y = num % 10
        w = self.convert(mapping, x)
        return w * 10 + mapping[y]
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x: self.convert(mapping, x))