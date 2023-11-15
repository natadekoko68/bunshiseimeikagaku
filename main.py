
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


n = 11
n_iter = 1000
alpha = 0.1
gamma = 0.99
rewards = [0 for _ in range(n)]
rewards[9] = 1
values = [0 for _ in range(n)]
ims = []


def reward(v,r):
    for k in range(n - 1):
        v[k] = round(v[k] + alpha * (r[k+1] + gamma * v[k + 1] - v[k]),3)
    v[0] = 0
    return v

for i in range(n_iter):
    values = reward(values, rewards)
    im = plt.plot(values)
    ims.append(im)
print(values)

# fig = plt.figure()
#
# # 10枚のプロットを 100ms ごとに表示
# ani = animation.ArtistAnimation(fig, ims, interval=100)
plt.show()

"""
0,0,0,1
0,0,0.2,0
0.2+0.2*(1+0.9*0-0)
0+0.2*(0+0.9*0.2-0)
"""