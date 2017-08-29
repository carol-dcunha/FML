import scipy as sp 

data=sp.genfromtxt("https://raw.githubusercontent.com/tomzaragoza/learning-ml-python/master/ch01/data/web_traffic.tsv",delimiter="\t")
x=data[:,0]
y=data[:,1]

x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]

def error(f,x,y):
	return sp.sum((f(x)-y)**2)

fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True)

f1=sp.poly1d(fp1)
fx=sp.linspace(0,x[-1],1000) #generate X-values for plotting
print "Error f1:",(error(f1,x,y))

fp2=sp.polyfit(x,y,2)
f2=sp.poly1d(fp2)
print "Error f2:",(error(f2,x,y))

fp3=sp.polyfit(x,y,3)
f3=sp.poly1d(fp3)
print "Error f3:",(error(f3,x,y))

fp10=sp.polyfit(x,y,10)
f10=sp.poly1d(fp10)
print "Error f4:",(error(f10,x,y))

import matplotlib.pyplot as plt 
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])

plt.plot(fx,f1(fx),linewidth=4)

plt.plot(fx,f2(fx),linewidth=4)

plt.plot(fx,f3(fx),linewidth=4)

plt.plot(fx,f10(fx),linewidth=4)
plt.legend(["d=%i"%f1.order,"d=%i"%f2.order,"d=%i"%f3.order,"d=%i"%f10.order],loc="upper left")

plt.autoscale(tight=True)
plt.grid()
plt.show()



