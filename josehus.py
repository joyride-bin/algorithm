# encoding = 'utf-8'

# 方法1
def josehus(n, m):
    """
    n: 人数
    m: 间隔的数量
    """
    people = list(range(1, n+1))
    out = []    #用来输出最后一个数的位置，第几位
    index = 0
    for i in range(n):   # 对列表做一次循环，每次出一人。
        count = 0
        while count < m:
            if people[index] != 0:
                count += 1
            if count  == m:
                out.append(people[index])
                people[index] = 0
            index = (index + 1) % n    # 使index循环指向列表的
    print(out[-1])
    return
if __name__ == '__main__':
    josehus(10,6)
            
