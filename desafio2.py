from typing import List, Tuple

def find_min_diff_pairs(nums: List[int], allow_duplicates: bool = True, 
                        sorted_pairs: bool = False, unique_pairs: bool = False) -> List[Tuple[int, int]]:
    
    nums.sort()
    min_diff = float('inf')
    result = []

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if diff < min_diff:
                min_diff = diff
                result = [(nums[i], nums[j])]
            elif diff == min_diff:
                result.append((nums[i], nums[j]))

    if not allow_duplicates:
        result = [pair for pair in result if pair[0] != pair[1]]
    if sorted_pairs:
        result = [tuple(sorted(pair)) for pair in result]
    if unique_pairs:
        result = list(set(result))
    
    return result
