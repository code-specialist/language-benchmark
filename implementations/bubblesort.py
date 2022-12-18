import sys
from typing import List


def bubble_sort(array: List[int]):
    for step in range(len(array) - 1):
        swapped = False
        for i in range(len(array) - step - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if swapped is False:
            break


if __name__ == "__main__":
    numbers_filename, list_length = sys.argv[1], int(sys.argv[2])
    numbers: List[int] = []

    with open(numbers_filename, "r") as numbers_file:
        for _ in range(list_length):
            numbers.append(int(numbers_file.readline().strip()))

    bubble_sort(numbers)
