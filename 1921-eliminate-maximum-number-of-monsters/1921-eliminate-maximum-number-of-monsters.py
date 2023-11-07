from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrivalTime = [(d - 1) // s for d, s in zip(dist, speed)]

        # Sort arrival times
        arrivalTime.sort()

        # Check if the weapon can be used before a monster arrives
        for i in range(n):
            if i > arrivalTime[i]:
                return i

        # All monsters can be eliminated
        return n