 from scipy.stats import geom
 import numpy as np
 import matplotlib.pyplot as plt
 sample=int(1000000)
 d=0
 n=0
 p = np.random.random(1)
 for i in range(sample):
   r = geom.rvs(p, size=2) #r[0] indicates the value of X1 and r[1] indicats the value of x2
   if (r[0]+r[1]==4):
     d=d+1
   if (r[0]+r[1]==4) and (r[0]==2):
     n=n+1
 probab_sim=n/d
 k=2
 x=4
 p_x=0
 for k in range(1,4):
   x1=geom.pmf(k, p, loc=0)
   x2=geom.pmf(x-k, p, loc=0)
   p_x=p_x+(x1*x2)
 a=geom.pmf(2, p, loc=0)*geom.pmf(2, p, loc=0)/p_x # using independence of x1 x2
 probab_theo=a
 x = np.arange(1)
 plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.25, label = 'Theoretical')
 plt.bar(x + 0.25, probab_sim, color = 'g', width = 0.25, label = 'Sim')
 #plt.xlabel('X=0')
 plt.ylabel('Probability')
 plt.xticks(x  + 0.25/2,['X1=2|X1+X2=4'])
 plt.legend()
 plt.show()
 print(f'The theoretical probability is {probab_theo} and the simulated probability is {probab_sim}')
 
 