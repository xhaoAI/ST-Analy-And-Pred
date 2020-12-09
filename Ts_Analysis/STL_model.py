# -*- coding: utf-8 -*-
# @author: Yihao
# @date: 2020-12
'''STL decomposition'''
from statsmodels.datasets import co2
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
data = co2.load(True).data
data = data.resample('M').mean().ffill()

from statsmodels.tsa.seasonal import STL
res = STL(data).fit()
res.plot()
plt.show()