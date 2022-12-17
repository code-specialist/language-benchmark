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


if __name__ == '__main__':
    list_input = eval(sys.argv[1])
    bubble_sort(unsorted_list=list_input)
