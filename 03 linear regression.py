import numpy as np
import matplotlib.pyplot as plt

#resist val (x)
r = (3.63, 3.37, 2.90, 2.52, 2.25, 2.07, 1.89, 1.64)
#temp val (y)
t = (14.1, 16.2, 19.1, 22.3, 25.2, 27.2, 29.2, 32.3)

#convert to vector
rv = np.array(r)
tv = np.array(t)

# 1 means
avg_r = np.mean(rv)
avg_t = np.mean(tv)

# 2 dot
numerator = (rv - avg_r).dot(tv - avg_t)
denom = np.sum((rv - avg_r)**2)

b = numerator/denom
a =  avg_t - b * avg_r

#print(f"y = {a:.3f} + {b:.3f} * x")

#---------- plot ----------------

x = np.arange(1.5, 4.1, 0.1) # start end step
y = [a + b * item for item in x]

plt.close('all')
plt.plot(r, t, '+b', label = 'measurements')
plt.plot(x,y,'-r', label='regression')
plt.legend()
plt.xlabel("Resistance (kOhm)")
plt.ylabel("Temperature C")
plt.show()

