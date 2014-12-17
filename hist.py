import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("hist.csv")

plt.hist(data, np.max(data) + 1, color="royalblue")
plt.ylabel("Participants")
plt.xlabel("Networks in SSID list")
plt.savefig("hist.pdf", format="pdf")
