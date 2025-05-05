import matplotlib.pyplot as plt
import numpy as np

# Players Run data.
sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

# Years of data.
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

# Last 5 years run data with sum.
sachin_5 = np.sum(sachin[5:])
sehwag_5 = np.sum(sehwag[5:])
kohli_5 = np.sum(kohli[5:])

# Plotting the data.
players = ["sachin", "sehwag", "kohli"]
last_5Year = [sachin_5, sehwag_5, kohli_5]

# Create a horizontal bar chart.
plt.barh(players,last_5Year)

# Add data labels to the bars.
for i in range(len(players)):
    plt.text(last_5Year[i]+50, i, str(last_5Year[i]), va='center')

# Add grid lines and set limits.
plt.grid(axis='x', linestyle='--', alpha=1.0)
plt.xlim(0, max(last_5Year) + 1000)

# Add labels and title.
plt.xlabel("Total Runs in Last 5 Years")
plt.ylabel("Player")
plt.title("Last 5-Year Performance of Indian Batsmen")
plt.tight_layout()
plt.show()