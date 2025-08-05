class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = []
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j] and j not in used:
                    n -= 1
                    used.append(j)
                    break

        return n
