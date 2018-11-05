# -*- coding: utf-8 -*-

def quickly_sort(alist):
    left = 0
    right = len(alist) -1
    quickly_sort_help(alist, left, right)
    return alist
    
def quickly_sort_help(alist, left, right):
    if left < right:
        split_point = partition(alist, left, right)
        quickly_sort_help(alist, left, split_point)
        quickly_sort_help(alist, split_point+1, right)
    else:
        return
def partition(alist, left, right):
    i  = left
    item = alist[right]
    for j in range(left, right):
        if alist[j] <= item:
            tmp = alist[j]
            alist[j] = alist[i]
            alist[i] = tmp
            i += 1
    alist[right] = alist[i]
    alist[i] = item
    return i-1
# 特别注意：这里返回的是i-1, 如果返回i的话会导致递归停止不了
alist = [10, 9, 8 , 6, 4, 3, 5, 3, 4, 5, 6, 8, 9, 10]
new_alist = quickly_sort(alist)
print(new_alist)
