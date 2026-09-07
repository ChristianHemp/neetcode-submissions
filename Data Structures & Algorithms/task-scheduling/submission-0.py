from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1
        
        max_freq = max(counts.values())
        num_max = 0

        for count in counts.values():
            if count == max_freq:
                num_max += 1
        
        return max((max_freq - 1) * (n + 1) + num_max, len(tasks))