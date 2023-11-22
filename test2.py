import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use('cyberpunk')

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 67, 19, 45, 10]
colors = ["C0", "C1", "C2", "C3", "C4"]

bars = plt.bar(categories, values, color=colors, zorder=2)

mplcyberpunk.add_bar_gradient(bars=bars)

plt.show()
