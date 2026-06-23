class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        maxNum = 10 ** 4
        l = maxNum.bit_length()
        offset = 1 << (l-1).bit_length()
        for i in range(len(arr)):
            arr[i] |= arr[i].bit_count() << offset
        arr.sort()
        for i in range(len(arr)):
            arr[i] &= (1 << offset) - 1
        return arr