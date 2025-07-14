import matplotlib.pyplot as plt


input_values = range(1, 1001)
squares = [x**2 for x in input_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, s=10)

# 设置标题和标签
ax.set_title('Scatter Plot Example', fontsize=24)
ax.set_xlabel("X-axis Label", fontsize=14)
ax.set_ylabel("Y-axis Label", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(labelsize=14)

# 设置x轴和y轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style='plain')

plt.show()