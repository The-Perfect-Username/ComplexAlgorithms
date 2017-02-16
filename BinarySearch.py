## Binary Search Algorithm

## Requires the list of elements to be
## sorted in either ascending or descending order

def bindarySearch(list, item):
    ## Init variables
    first = 0
    last = len(list) - 1
    found = False

    ## Loop through list as long as the the item is not found and until all
    ## elements have been searched
    while first <= last and not found:
        ## Find the midpoint of the list
        middle = (first + last)//2
        ## If the middle element of the search area of the list is equal
        ## to the search item, then the item is found. Otherwise if it is
        ## less than, set the first index to equal the middle index + 1; or
        ## set the last index to equal the middel index - 1 to half the search
        ## area
        if list[middle] == item:
            found = True
            return found
        elif list[middle] < item:
            first = middle + 1
        else:
            last = middle - 1

    ## If item not found then return false
    return False

array = [1, 2, 4, 5, 6, 7, 12, 13, 13, 15, 16, 19, 20, 21, 23, 25, 31, 34, 50]

itemFound = bindarySearch(array, 4)

if itemFound:
    print "Item has been found!"
else:
    print "Item was not in the list"
