#2
import scipy.stats

z = scipy.stats.norm(0,1)
p = 1-z.cdf(1-1.1) 
print(p) #0.5398278372770291