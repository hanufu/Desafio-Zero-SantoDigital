from desafio1 import generate_asterisks
from desafio2 import find_min_diff_pairs
from desafio3 import find_all_subsets
from desafio_avancado_2 import find_min_diff_pairs_advanced
from desafio_avancado_3 import find_all_subsets_advanced

def main():
    print("Desafio 1:")
    n = 5
    print(generate_asterisks(n))

    print("\nDesafio 2:")
    nums = [4, 9, 1, 32, 13]
    print(find_min_diff_pairs(nums))

    print("\nDesafio 3:")
    nums = [1, 2]
    print(find_all_subsets(nums))

    print("\nDesafio Avançado II:")
    nums = [4, 9, 1, 32, 13]
    print(find_min_diff_pairs_advanced(nums, allow_duplicates=False, sorted_pairs=True, unique_pairs=True))

    print("\nDesafio Avançado III:")
    nums = [1, 2, 2]
    print(find_all_subsets_advanced(nums, max_size=2, min_size=1, distinct_only=True, sort_subsets=True))

if __name__ == "__main__":
    main()
