# Consider an array of non-negative integers. A second array is form by shuffling the elements of the first array
# and deleting a random element. Given these two arrays, find which element is missing in the second array.

import collections

def finder2(arr1,arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1

arr1 = [5,5,7,7]
arr2 = [5,7,7]

finder2(arr1,arr2)

