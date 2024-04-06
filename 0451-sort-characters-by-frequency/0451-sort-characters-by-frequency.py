class Solution:
    def frequencySort(self, s: str) -> str:
        char_counter = Counter(s)
        char_frequences = [[] for _ in range(len(s) + 1)]
        
        for char, amount in char_counter.items():
            char_frequences[amount] += [char]
        
        result = ""
        for amount in range(len(char_frequences) - 1, 0, -1):
            for char in char_frequences[amount]:
                result += char * amount
                
        return result