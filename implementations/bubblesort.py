import sys
from typing import List


def bubble_sort(unsorted_list: List) -> List:
    number_of_changes = 0
    for index in range(len(unsorted_list) - 1):
        if unsorted_list[index] > unsorted_list[index + 1]:
            unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]  # swap
            number_of_changes += 1
    if number_of_changes > 0:
        return bubble_sort(unsorted_list[:-1]) + [unsorted_list[-1]]
    return unsorted_list


if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    numbers_filename, list_length = sys.argv[1], int(sys.argv[2])
    numbers: List[int] = []

    with open(numbers_filename, "r") as numbers_file:
        for _ in range(list_length):
            numbers.append(int(numbers_file.readline().strip()))

    sorted_list = bubble_sort(numbers)
