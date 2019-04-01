
from matplotlib import pyplot as plt

years = [ 1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [ 300.2, 543, 1075, 2862.2, 599.6, 20189, 14958]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nonimal GDP")
plt.ylabel("Trillions of $")
# plt.show()




