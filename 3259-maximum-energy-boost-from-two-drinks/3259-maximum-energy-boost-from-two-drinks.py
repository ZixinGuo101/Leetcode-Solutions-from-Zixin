class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        wait = 0
        ea = -inf
        eb = -inf
        for i in range(n):
            prev_w = wait
            wait = max(ea, eb)
            ea = max(ea, prev_w) + energyDrinkA[i]
            eb = max(eb, prev_w) + energyDrinkB[i]
        return max(ea, eb)