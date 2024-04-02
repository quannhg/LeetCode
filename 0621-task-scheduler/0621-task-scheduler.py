class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        amount_char = {}
        max_amount = max_chars_amount = 0
        
        # find max amount char
        for task in tasks:
            if task in amount_char:
                amount_char[task] += 1
            else:
                amount_char[task] = 1
                
            if amount_char[task] == max_amount:
                max_chars_amount += 1
            elif amount_char[task] > max_amount:
                max_chars_amount =  1
                max_amount = amount_char[task]
        
        empty_slot_amount = (max_amount - 1) * (n - max_chars_amount + 1)
        available_task_amount = len(tasks) - (max_chars_amount * max_amount)
        
        idle_slot = max(0, empty_slot_amount - available_task_amount)
        
        return len(tasks) + idle_slot
                
            
            