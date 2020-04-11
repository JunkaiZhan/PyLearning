
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(20)
x = range(len(y))

sw = 11

if sw == 1:
    plt.figure(figsize=(7,5))
    plt.plot(x, y, 'b', lw=1.5, label='1st')            # 画线，设置线颜色和线宽
    plt.plot(y, 'ro')                                   # 画点，设置点颜色和形状
    plt.plot(x, y.cumsum(), 'g', lw=1.5, label='2nd')   # 画另一条线
    plt.plot(y.cumsum(), 'yo')             # 画另一组点
    plt.grid(True)                         # 添加网格线
    plt.axis("tight")                      # 紧凑坐标系
    plt.xlabel('index')                    # 设置横坐标
    plt.ylabel('value')                    # 设置纵坐标
    plt.title('A Simple Plot')             # 设置图题
    plt.legend(loc=0)
    plt.show()
elif sw == 2: # 画两个子图
    plt.figure(figsize=(7, 7))
    plt.subplot(211)
    plt.plot(y, lw=1.5, label='1st')
    plt.plot(y, 'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.ylabel('value')
    plt.title('HelloWorld 1')
    plt.subplot(212)
    plt.plot(y, lw=1.5, label='2nd')
    plt.plot(y, 'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('HelloWorld 2')
    plt.show()
elif sw == 3: # 画线图点图和柱状图结合
    np.random.seed(2000)
    y = np.random.standard_normal((20,2)).cumsum(axis=0)
    plt.figure(figsize=(9, 4))
    plt.subplot(121)
    plt.plot(y[:, 0], lw=1.5, label='1st')
    plt.plot(y[:, 0], 'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.ylabel('value')
    plt.title('HelloWorld 1')
    plt.subplot(122)
    plt.bar(range(len(y[:, 1])), y[:, 1], width=1.5, color='g', label='2nd')
    plt.grid(True)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('HelloWorld 2')
    plt.show()
elif sw == 4: # 两个Y轴
    y = np.random.standard_normal((20,2)).cumsum(axis=0)
    y[:, 0] = y[:, 0] * 100
    fig, ax1 = plt.subplots()
    plt.plot(y[:, 0], lw=1.5, color='g', label='1st')
    plt.grid(True)
    plt.legend(loc=8)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A Simple Plot')
    ax2 = ax1.twinx()
    plt.plot(y[:, 1], lw=1.5, color='r', label='2nd')
    plt.legend(loc=0)
    plt.show()
elif sw == 5: # 散点图
    y = np.random.standard_normal((1000, 2))
    plt.figure(figsize=(7, 5))
    plt.plot(y[:, 0], y[:, 1], 'ro')
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')
    plt.show()
elif sw == 6: # 散点图专用函数
    y = np.random.standard_normal((1000, 2))
    c = np.random.randint(0, 10, len(y))
    plt.figure(figsize=(7, 5))
    plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
    plt.colorbar()
    plt.grid(True)
    plt.xlabel('1st')
    plt.ylabel('2nd')
    plt.title('Scatter Plot')
    plt.show()
elif sw == 7: # 直方对比图
    y = np.random.standard_normal((1000, 2))
    plt.figure(figsize=(7, 4))
    plt.hist(y, label=['1st', '2nd'], bins=25)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title('Histogram')
    plt.show()
elif sw == 8: # 直方图堆叠
    y = np.random.standard_normal((1000, 2))
    plt.figure(figsize=(7, 4))
    plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=50)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title('Histogram')
    plt.show()
elif sw == 9: # 箱型图
    y = np.random.standard_normal((1000, 2))
    fig, ax = plt.subplots(figsize=(7,4))
    plt.boxplot(y)
    plt.grid(True)
    plt.setp(ax, xticklabels=['1st', '2nd'])
    plt.xlabel('data set')
    plt.ylabel('value')
    plt.title('Boxplot')
    plt.show()
elif sw == 10: # 3D图
    strike = np.linspace(50, 150, 24)
    ttm = np.linspace(0.5, 2.5, 24)
    strike, ttm = np.meshgrid(strike, ttm)
    iv = (strike - 100) ** 2 / (100 * strike) / ttm
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(9,6))
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)
    ax.set_xlabel('strike')
    ax.set_ylabel('time-to-maturity')
    ax.set_zlabel('implied volatility')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()
elif sw == 11: # 3D三点图
    strike = np.linspace(50, 150, 24)
    ttm = np.linspace(0.5, 2.5, 24)
    strike, ttm = np.meshgrid(strike, ttm)
    iv = (strike - 100) ** 2 / (100 * strike) / ttm
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(30, 60)
    ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')
    ax.set_xlabel('strike')
    ax.set_ylabel('time-to-maturity')
    ax.set_zlabel('implied volatility')
    plt.show()
