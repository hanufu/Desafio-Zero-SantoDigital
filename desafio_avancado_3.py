from itertools import chain, combinations
from typing import List

def find_all_subsets_advanced(nums: List[int], max_size: int = None, min_size: int = None,
                              distinct_only: bool = False, sort_subsets: bool = False) -> List[List[int]]:
    
    if distinct_only:
        nums = list(set(nums))
    
    all_subsets = list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))
    
    if min_size is not None:
        all_subsets = [subset for subset in all_subsets if len(subset) >= min_size]
    if max_size is not None:
        all_subsets = [subset for subset in all_subsets if len(subset) <= max_size]
    
    if sort_subsets:
        all_subsets = [sorted(list(subset)) for subset in all_subsets]
        all_subsets.sort()

    return [list(subset) for subset in all_subsets]
