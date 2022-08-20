from hilbert_curve import hilbex_to_cartesian
import numpy as np
import matplotlib.pyplot as plt

coords = []

h_idx = 200000
for i in range(h_idx):
    coords.append(hilbex_to_cartesian(i, h_idx))
    print(i, hilbex_to_cartesian(i, h_idx))

coords = np.array(coords)

plt.plot(coords[:, 0])
plt.plot(coords[:, 1])
plt.show()