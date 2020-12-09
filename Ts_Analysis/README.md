[toc]
# 时间序列分解
## 一、STL分解

STL分解是时间序列分解里常用的方法，基于LOESS（局部加权回归）将时间序列分解成**趋势分量、季节分量和余项**。

<img src="https://mmbiz.qpic.cn/mmbiz_png/FIzOEib8VQUqqPuNR2PrLA18XEPB4zXnELp2fxOzsptdJHpiaSgBtj0rDSgWSD4jmUXWiaknzUjA0XUndJ3D48Zlg/640?wx_fmt=png&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1,z" alt="img" style="zoom:67%;" />

### STL的优势
- 可以处理任何类型的季节性
- 允许季节成分随时间变化，并且变化的速率可以变化
- 季节随时间变化速率以及TC的平滑性都可以自定义
- 对异常值不敏感

### STL的缺点
- 只有加法模式
- 不能自动处理日历变动或交易日影响

## 二、小波变换


## 三、傅里叶变换
