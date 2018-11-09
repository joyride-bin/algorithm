
# -*- coding='utf-8' -*-

def binary_search(alist, target):
    """
    alist: 有序列表
    """
    left = 0
    right = len(alist)-1
    while left <= right:
        middle = (right - left)//2
        if alist[middle] < target:
            left = middle+1
        elif alist[middle] > target:
            right = middle-1
        else: return middle
    return -1
alist = [1, 3, 5, 7, 9, 11]
target = 7

binary_search(alist, target)
