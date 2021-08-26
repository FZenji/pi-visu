import matplotlib.pyplot as plt
import numpy as np
import main

pi_bearing = [[0], [0]]
pi = main.pi_list(10000)
for i in range(len(pi)):
    bearing = 36 * pi[i]
    pi_bearing[0].append(pi_bearing[0][i] + np.sin(np.radians(bearing)))
    pi_bearing[1].append(pi_bearing[1][i] + np.cos(np.radians(bearing)))

plt.scatter(pi_bearing[0], pi_bearing[1])
plt.plot(pi_bearing[0], pi_bearing[1])
plt.show()
