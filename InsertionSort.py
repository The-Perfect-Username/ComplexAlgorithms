## Insertion Sort Algorithm

## Sorts an unordered list of elements in ascending order
## Iterates through each element of the array and store the current
## element into a temporary variable to be compared to all previous elements.
## The previous elements are all shifted to the right if they are larger than
## the current element, until the comparison condition is not longer met

def insertionSort(list):
    length = len(list)

    for i in range(1, length):
        item = list[i]
        index = i - 1
        while index >= 0 and list[index] > item:
            list[index + 1] = list[index]
            index = index - 1

        list[index + 1] = item
    return list


array = [1, 4, 2, 99, 32, 2, 8, 43, 23, 90, 401, 3890, 23, 1232, 42, 4, 232, 193, 232]
print insertionSort(array)
