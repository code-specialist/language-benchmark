import sys
from typing import List


def bubble_sort(array: List[int]):
    i, n, swap_needed = 0, len(array), True

    while i < n - 1 and swap_needed:
        swap_needed = False

        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swap_needed = True

        if not swap_needed:
            break

        i += 1


if __name__ == "__main__":
    numbers_filename, list_length = sys.argv[1], int(sys.argv[2])
    numbers: List[int] = []

    with open(numbers_filename, "r") as numbers_file:
        for _ in range(list_length):
            numbers.append(int(numbers_file.readline().strip()))

    bubble_sort(numbers)
