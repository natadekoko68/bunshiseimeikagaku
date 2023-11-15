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

ims_tds = []

def reward(v,r):
    t = [0 for _ in range(n)]
    for k in range(n - 1):
        t[k] = r[k+1] + gamma * v[k + 1] - v[k]
    t[0] = 0
    for k in range(n - 1):
        v[k] = round(v[k] + alpha * (r[k+1] + gamma * v[k + 1] - v[k]), 3)
    v[0] = 0
    return v, t

for i in range(n_iter):
    values, tds = reward(values, rewards)
    im = plt.plot(values)
    # im2 = plt.plot(tds)
    # ims.append(im)
print(values)

plt.show()
