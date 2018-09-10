from matplotlib import pylab
import seaborn as sns

from com.hhj.uqer.seven.demo2 import portfolioSize, timeSpent

print('demo3 %s' % __name__)

sns.set(style="ticks")
pylab.figure(figsize=(12, 8))
pylab.bar(portfolioSize, timeSpent, color='r', width=300)
pylab.grid(True)
pylab.title('calc cost seconds',  fontsize=18)
pylab.ylabel('time(s)',  fontsize=15)
pylab.xlabel('count',  fontsize=15)
pylab.show()

