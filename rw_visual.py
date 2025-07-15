import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个随机漫步实例
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 绘制随机漫步的点
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=125)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
    ax.scatter(0, 0, s=100, c='green', edgecolor='none')  # 起点
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red', edgecolor='none')  # 终点
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break