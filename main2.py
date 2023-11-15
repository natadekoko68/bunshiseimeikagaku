"""
壁の座標を保持?
x軸に平行な壁、y軸に平行な壁
"""

a = """
S__#____
_#_#__#_
_#_#__#_
_#____#_
_######_
_______G
"""

maze = list(a.split())
print(maze)

height = len(maze)
width = len(maze[0])

for i in range(height):
    for j in range(width):
        if maze[i][j] == "S":
            s = i, j
        if maze[i][j] == "G":
            g = i, j

queue = [(s, 0)]

visited = {s: 0}

move_x = [0,0,1,-1]
move_y = [1,-1,0,0]

while queue:
    t,num = queue.pop()
    if t == g:
        print("goal",num)
    else:
        for i in range(4):
            next_x = t[1] + move_x[i]
            next_y = t[0] + move_y[i]
            if (0 <= next_x < width) and (0 <= next_y < height) and (maze[next_y][next_x]!="#") and (((next_y,next_x) not in visited) or (visited[(next_y,next_x)] >= num + 1)):
                queue.append(((next_y,next_x),num+1))
                visited[(next_y,next_x)] = num + 1

value = [[0 for i in range(width)] for j in range(height)]
for i in range(height):
    for j in range(width):
        if maze[i][j] == "#":
            value[i][j] = -1
        else:
            pass
        if (i == height-1) and (j == width-1):
            value[i][j] = 10



for i in range(height):
    temp = []
    for j in range(width):
        temp.append(str(value[i][j]))
    print("\t".join(temp))








