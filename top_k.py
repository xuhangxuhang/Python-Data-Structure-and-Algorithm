# Author_='Jimmy.Xu'
# Time: 2022/1/11  0:52
# FileName:top_k.py

def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]

    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def top_k(li, k):
    heap = li[:k]

    n = len(li)
    for i in range(k//2 - 1, -1, -1):
        sift(heap, i, k - 1)

    for i in range(k, n):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)

    return heap


li = [i for i in range(100)]
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)
heap = top_k(li, 100)
print('排序结果')
print(heap)
