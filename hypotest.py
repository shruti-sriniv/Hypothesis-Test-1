import numpy as np
import math
from scipy.stats import t
# Input: numpy vector a of scalar values, with k rows, 1 column
# numpy vector b of scalar values, with k rows, 1 column
# scalar alpha
# Output: reject (0 or 1)
def run(a,b,alpha):
    # Your code goes here
    k, d = np.shape(a)
    mu1 = 0
    mu2 = 0
    sigma2_1 = 0
    sigma2_2 = 0
    for i in range(0, k):
        mu1 += a[i]
        mu2 += b[i]

    mu1 /= k
    mu2 /= k

    for j in range(0, k):
        sigma2_1 += (a[j] - mu1)**2
        sigma2_2 += (b[j] - mu2)**2

    sigma2_1 /= k
    sigma2_2 /= k

    x = ((mu1 - mu2) * math.sqrt(k)) / (math.sqrt((sigma2_1 ** 2) + (sigma2_2 ** 2)))
    v = np.ceil((((sigma2_1 + sigma2_2) **2) * (k -1)) / ((sigma2_1 **2) + (sigma2_2 ** 2)))

    if x > t.ppf(1 - alpha, v):
        reject = 1
    else:
        reject = 0

    return reject