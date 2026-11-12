#---------------------------prog01------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
ypoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#ypoints2 = np.array([1, 3, 5, 7, 9])
#xpoints2 = np.array([1, 2, 3, 4, 5])

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")

plt.plot(xpoints, ypoints, ls=':',c="blue")
#plt.plot(xpoints2, ypoints2, ls='-',c="hotpink")
plt.show()


import pandas as pd

data = {
    "X": xpoints,
    "Y": ypoints
}
df = pd.DataFrame(data)
print(df)


