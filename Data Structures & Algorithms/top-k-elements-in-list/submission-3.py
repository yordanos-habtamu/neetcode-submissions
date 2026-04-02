from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        # Count occurrences by grouping into lists
        for i in nums:
            if i not in groups:
                groups[i] = []
            groups[i].append(i)

        # Convert each group to (number, count)
        freq_list = [(num, len(group)) for num, group in groups.items()]

        # Sort by frequency (largest → smallest)
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # Extract top k numbers
        result = [num for num, count in freq_list[:k]]

        return result
