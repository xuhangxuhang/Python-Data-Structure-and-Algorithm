# Author_='Jimmy.Xu'
# Time: 2022/1/6  23:46
# FileName:heap_sort.py


def sift(li, low, high):
    '''
    构造堆
    :param li:输入列表
    :param low:堆得堆顶下标
    :param high:堆得最后一个元素的下标，作用是限制列表不越界
    :return:
    '''
    i = low # 指向当前层的层数，最开始指向根节点
    j = 2 * i + 1 # 节点的左子节点
    tmp = li[low] # 把堆顶元素存起来
    # while j <= high and j + 1 <= high: # 第一个判断条件：保证左孩子节点值不越界 第二个判断条件：右子节点不越界
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]: # 第一个判断条件：保证左孩子节点值不越界 第二个判断条件：右子节点不越界
            j = j + 1 # 如果右子节点的值大于左子节点，那就指向右子节点，看右边分支
        if li[j] > tmp: # 子节点的值比tmp的大，
            li[i] = li[j] # 就把子节点的值放到其父节点的位置
            i = j # 然后把下标指向子该节点，再比较子节点与其子节点的值的大小，更新父节点和子节点的值
            j = 2 * i + 1
        else: # tmp的值比子节点的值更大，那就把tmp放到j所指的位置，此时按照堆得性质，就说明已经把tmp放到了当前子堆得最大位置
            li[i] = tmp
            break
    else: # 如果遍历了整个堆的父节点元素后发现都没有找到最大值，那就需要把tmp的值放到叶子节点的位置上
        li[i] = tmp

def heap_sort(li):
    n = len(li)
    # 先建堆，从最小堆开始找，"农村包围城市"，那就需要找到最后一个节点
    # 如何找到一个节点--从孩子找父亲
    # 如何找到最后一个节点？--从最后一个叶子节点找父节点，又因为堆是一颗完全二叉树，如果设子节点是i，那父节点就是(i-1)//2
    # 回到问题，如果i是最后一个叶子节点，那节点的下标就是i = len(li) - 1, 找父节点的话就是i = (i - 1) // 2 = (n - 1 - 1) // 2 = (n - 2) // 2 = n//2 - 1
    for i in range(n//2 - 1, -1, -1): # 此时i就代表所有待调整子堆得根节点的元素下标
        sift(li, i, n - 1) # sift(li, low, high)函数中，high的作用是防止堆的最大元素越界，因为子堆的high元素不好求（如果子堆有大于2层）
                           # 所以就直接让整个堆的最后一个元素作为high就行了--->需要回顾sift函数中high的作用
    # 循环完成后堆就简历完成了

    #
    for i in range(n - 1, -1, -1): # i指向当前堆中最后一个元素
        li[0], li[i] = li[i], li[0] # 完成堆顶元素和最后一个叶子节点的叫唤
        sift(li, 0, i - 1) # 完成交换后，high应该指向倒数第二个元素，此时原本的堆顶元素（省长）已经拿出来放到最后一个元素，不在搜索范围之内了



import random
import math
li = [i for i in range(100)]
random.shuffle(li)
print(li)
heap_sort(li)
print(li)
#
# for i in li:
#     if math.log2(i)%2==0 or math.log2(i)%2==1:
#         print(i, end = '\n')
#     else:
#         print(i, end = ' ')
