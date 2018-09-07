from math import log, sqrt, exp
from scipy.stats import norm


def call_option_pricer(spot, strike, maturity, r, vol):
    d1 = (log(spot / strike) + (r + 0.5 * vol * vol) * maturity) / vol / sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)

    price = spot * norm.cdf(d1) - strike * exp(-r * maturity) * norm.cdf(d2)
    return price


if __name__ == '__main__':
    print(call_option_pricer(2.45, 2.50, 0.25, 0.05, 0.25))
