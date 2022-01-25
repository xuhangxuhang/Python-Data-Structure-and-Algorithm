# Author_='Jimmy.Xu'
# Time: 2022/1/25  23:17
# FileName:maze.py

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
