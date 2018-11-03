# python
def insert_sort(alist):
    for key, value in enumerate(alist):
        index = key
        while index > 0 and alist[index - 1] > value:
            alist[index] = alist[index -1]
            index -= 1
        alist[index] = value
    return alist
    
alist = [54,26,93,17,77,31,44,55,20]
print(insert_sort(alist))

def insert_sort2(alist) :
    for i in range(len(alist)):
        tmp = alist[i]
        index = i
        while index > 0 and alist[index-1] > tmp:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = value
    return alist
    
print(inert_sort2)
