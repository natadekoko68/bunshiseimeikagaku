class Maze:
    def __init__(self,h,w):
        self.width = w
        self.height = h
        self.walls = []

    def input_maze(self,filepath):
        cnt = -1
        with open(filepath) as f:
            for line in f:
                # print(line.split("+"))
                line = line.rstrip()
                cnt += 1
                if cnt % 2 == 0:
                    # print(line)
                    for i in range(self.width):
                        num = i*4+1
                        if line[num] == "-":
                            self.walls.append((cnt//2,i,"up"))
                        else:
                            pass
                else:
                    # print(line.replace(" ","_"))
                    for i in range(self.width+1):
                        num = i*4
                        if line[num] == "|":
                            self.walls.append(((cnt-1)//2,i,"left"))
                        else:
                            pass


a = Maze(4,5)
a.input_maze("/Users/kotaro/PycharmProjects/分子生命科学/test.txt")
print(a.walls)
