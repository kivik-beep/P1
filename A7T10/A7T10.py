import numpy as np
import matplotlib.pyplot as plt
import statistics

mu,sigma = 0, 0.1 #mean and standard deviation
v = np.random.normal(mu, sigma, 1000000)


#plot the values
count, bins, ignored = plt.hist(v, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.savefig("histogram.png")
plt.show()

#plot the ECDF
x, counts = np.unique(v, return_counts=True)
cumsum = np.cumsum(counts)
y = cumsum / cumsum[-1]

x = np.insert(x, 0, x[0])
y = np.insert(y, 0, 0.)
plt.xlabel("Value")
plt.ylabel("%")
plt.title("CDF")
plt.plot(x, y, drawstyle="steps-post")
plt.grid(True)
plt.show()
plt.savefig("ecdf.png")

median = statistics.median(v)
print(f"median is {median}")
