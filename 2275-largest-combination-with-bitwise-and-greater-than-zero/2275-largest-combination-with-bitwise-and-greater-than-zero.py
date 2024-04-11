class Solution:    
    def largestCombination(self, candidates: List[int]) -> int:
        number_bit_1_at_index = Counter()
        for num in candidates:
            index = 0
            while num:
                if num % 2 == 1:
                    number_bit_1_at_index[index] += 1
                index += 1
                num //= 2
        return max(number_bit_1_at_index.values())