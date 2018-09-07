from math import log, sqrt, exp
from scipy.stats import norm


def call_option_pricer(spot, strike, maturity, r, vol):
    d1 = (log(spot / strike) + (r + 0.5 * vol * vol) * maturity) / vol / sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)

    price = spot * norm.cdf(d1) - strike * exp(-r * maturity) * norm.cdf(d2)
    return price
print('demo1 %s' % __name__)

if __name__ == '__main__':
    # 参数
    spot1 = 2.45
    strike1 = 2.50
    maturity1 = 0.25
    r1 = 0.05
    vol1 = 0.25

    print('期权价格 : %.4f' % call_option_pricer(spot1, strike1, maturity1, r1, vol1))
