import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

def PDF(x):
    t2 = (1/57)**2
    exponent = -0.5*t2*np.power(x,2)
    
    return t2*x*np.exp(exponent)
  
def CDF(x):
    t2 = (1/57)**2
    exponent = -0.5*t2*np.power(x,2)

    return 1-np.exp(exponent)
  
x = np.array(range(1000))
y = PDF(x)

x1 = np.array(range(1000))
y1 = CDF(x)   

# plot PDF
PDF = plt.plot(x,y)
plt.show()

# plot CDF
CDF = plt.plot(x1,y1)
plt.show()
