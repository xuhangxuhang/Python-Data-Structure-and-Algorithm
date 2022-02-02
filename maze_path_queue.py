#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time:2/2/2022 4:08 PM
# Author: Jimmy.Xu
from collections import deque
'''
广度优先搜索，和深度优先搜索的思想不同，

先比较二者走同一个迷宫的结果，二者搜索结果如下，可见在深度优先搜索中部分迷宫元素的值是0，而广度优先搜索的所有值都已经是变成了2
这是因为广度优先搜索每走到一个可能的点，会去搜索周围所有的可能走的路径，即、上下右（如果从左边走过来）三个方向均会搜索

使用队列实现广度优先搜索
建一个列表path来存储走过的路径，每个进队的元素都需要标记它是在哪个点给搜索出来的，再加上需要携带自身元素所在的坐标信息，队列中的单个元素就是三维的
前两个是坐标，最后一个是上个元素的下标

深度优先搜索：
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
 [1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
 [1, 2, 2, 2, 2, 1, 1, 2, 2, 2],
 [1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
 [1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
 [1, 2, 2, 2, 2, 2, 1, 2, 2, 1],
 [1, 2, 2, 1, 1, 0, 1, 1, 2, 1],
 [1, 1, 0, 0, 0, 0, 0, 0, 2, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
 
 广度优先搜索：
 [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 1, 2, 2, 2, 1, 2, 1],
 [1, 2, 2, 1, 2, 2, 2, 1, 2, 1],
 [1, 2, 2, 2, 2, 1, 1, 2, 2, 1],
 [1, 2, 1, 1, 2, 2, 2, 2, 2, 1],
 [1, 2, 2, 1, 2, 2, 2, 2, 1, 1],
 [1, 2, 1, 2, 2, 2, 1, 2, 2, 1],
 [1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
 [1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
 
'''
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def print_r(path):
    curNode = path[-1]
    realpath = []

    while curNode[-1] != -1:
        realpath.append(curNode[:2])
        curNode = path[curNode[-1]]
    realpath.append(curNode[:2])
    realpath.reverse()

    for item in realpath:
        print(item)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print('有路')
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print('没有路')
        return False
maze_path_queue(1, 1, 8, 7)
