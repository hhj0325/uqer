import time
import numpy as np

from com.hhj.uqer.seven.demo1 import call_option_pricer

print('demo2 %s' % __name__)
portfolioSize = range(1, 10000, 500)
timeSpent = []
# 参数
spot = 2.45
strike = 2.50
maturity = 0.25
r = 0.05
vol = 0.25


for size in portfolioSize:
    now = time.time()
    strikes = np.linspace(2.0, 3.0, size)
    for i in range(size):
        res = call_option_pricer(spot, strikes[i], maturity, r, vol)
    print(timeSpent)
    timeSpent.append(time.time() - now)
