from random import randint
from math import ceil


def peak_finding(arr):
    l = len(arr)-1
    mid = l//2
    if l == mid:
        return arr[mid],mid
    elif arr[mid] < arr[mid+1]:
        return peak_finding(arr[mid+1:])
    elif arr[mid] < arr[mid-1]:
        return peak_finding(arr[:mid])
    else: return arr[mid],mid


def peak_finding_non_recursion(arr):
    start = 0

    while True:
        l = len(arr)-1
        mid = l//2
        if l == mid:
            return f'peak-{arr[mid]}'
        elif arr[mid] < arr[mid+1]:
            start = mid
            arr = arr[start+1:]
        elif arr[mid] < arr[mid-1]:
            arr = arr[start:mid]
        else: return f'peak-{arr[mid]}'


def find_max(arr, mid):

    max = 0
    max_index = 0
    for i in range(len(arr)):
        if arr[i][mid] > max:
            max = arr[i][mid]
            max_index = i

    return max, max_index

def peak_finding_2D(arr, mid):

    rows = len(arr)
    columns = len(arr[0])
    max, max_index = find_max(arr, mid)
    if mid == len(arr[0])-1:
        return max,[max_index, mid]
    elif arr[max_index][mid+1] > max:
        return peak_finding_2D(arr, mid+ceil(mid/2))
    elif arr[max_index][mid-1] > max:
        return peak_finding_2D(arr, mid-ceil(mid/2))
    return max,[max_index, mid]








lis_2d = []


for i in range(15):
    lis_2d.append([])
    for j in range(15):
        lis_2d[i].append(randint(0,100))

for i in lis_2d:
    print(i)

print(peak_finding_2D(lis_2d, 0))


