## Median Algorithm

## Searches through an unsorted list of elements for the median value

def medianSearch(list):
    length = len(list)
    if length == 1:
        return list[0]
    else:
        middle = length//2
        return select(list, 0, middle, length - 1)

def select(list, first, middle, last):
    pos = partition(list, first, last)
    if pos == middle:
        return list[pos]

    if pos > middle:
        return select(list, first, middle, pos - 1)

    if pos < middle:
        return select(list, pos + 1, middle, last)

def partition(list, first, last):
    pivotal = list[first]
    pivotloc = first

    for i in range(first + 1, last + 1):
        if list[i] < pivotal:
            pivotloc += 1
            ## Swap elements
            list[pivotloc], list[i] = list[i], list[pivotloc]

    list[pivotloc], list[first] = list[first], list[pivotloc]

    return pivotloc


array = [1, 2, 3, 4, 9, 6, 7, 8, 5]
print medianSearch(array)
array = [4, 1, 10, 9, 7, 12, 8, 2, 15]
print medianSearch(array)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print medianSearch(array)
