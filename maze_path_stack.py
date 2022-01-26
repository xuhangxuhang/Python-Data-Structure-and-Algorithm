# Author_='Jimmy.Xu'
# Time: 2022/1/25  23:17
# FileName:maze.py
'''
通过栈实现走迷宫问题的思想：
迷宫问题，从起点开始，遇到0则走一步，走的方向可以上下左右任意，碰到1就换方向，碰到0就继续走。
可以按照一个固定顺序，从起点开始，上、右、下、左四个方向依次走（可以按照四个方向任意顺序）

使用一个栈来存储走的路径，
首先将起点放如栈中，然后按照既定方向依次寻找下一个点，将下一个元素压栈

遇到0就按照既定方向继续前进
遇到1就停止当前方向，转而寻找其他方向
如果所有方向都找不到前进方向，栈顶元素就出栈，转而回退回栈中的上一个元素开始找
走过的点可踹改为2，防止走回头路

上述逻辑可以用个while循环来实现
跳出while循环的判断条件是栈空
'''
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]
    
dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1) 
]
    
def maze_path(x1, y1, x2, y2):
    
    maze_height, maze_width = len(maze), len(maze[0])
    if x1 >= maze_height or x2 >= maze_height:
        print('error input value')
        return False
    if y1 >= maze_width or y2 >= maze_width:
        print('error input value')
        return False
    
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            print('找到路了!')
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('没有路')
        return False

maze_path(1,1,8,8)
maze_path(1,1,8,8)
