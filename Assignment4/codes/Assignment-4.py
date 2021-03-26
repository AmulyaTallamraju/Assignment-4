 from scipy.stats import geom
 import numpy as np
 import matplotlib.pyplot as plt
 import seaborn as sb
 sb.set()
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
 #calculating theoretical probability
 k=2
 x=4
 p_x=0
 for k in range(1,4):
   x1=geom.pmf(k, p, loc=0)
   x2=geom.pmf(x-k, p, loc=0)
   p_x=p_x+(x1*x2)
 a=geom.pmf(2, p, loc=0)*geom.pmf(2, p, loc=0)/p_x # using independence of x1 x2
 probab_theo=a

 print(f'The theoretical probability is {probab_theo} and the simulated probability is {probab_sim}')
b=[0,0,0,0,0,0,0,0,0,0]
p_x=0

i=2

while i <12:
  c=0
  for k in range(1,i):
    x1=geom.pmf(k, p, loc=0)
    x2=geom.pmf(i-k, p, loc=0)
    c=c+x1*x2
    
  
  b[i-2]=c[0]
  i=i+1
  
  


#plotting
fig,axes = plt.subplots(1,3, figsize=(15,5))
fig.suptitle('PMF')

x = np.arange(1,11)
dist=geom(p)
sb.barplot(ax=axes[0], x=x, y=dist.pmf(x))
axes[0].set(xlabel='X1', ylabel='p(X1)')
axes[0].set_title("PMF of X1")

dist=geom(p)
sb.barplot(ax=axes[1], x=x, y=dist.pmf(x))
axes[1].set(xlabel='X2', ylabel='p(X2)')
axes[1].set_title("PMF of X2")

x=np.arange(2,12)
dist=geom(p)
sb.barplot(ax=axes[2], x=x, y=b)
axes[2].set(xlabel='X', ylabel='p(X)')
axes[2].set_title("PMF of X")

# p=0.27047335 was the value used while plotting


 