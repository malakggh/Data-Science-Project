import numpy as np
import matplotlib.pyplot as plt

def get_ticks(bins, data):
    step = round(np.ptp(data)/bins)
    return np.arange(start=min(data),
                            step=step,
                            stop=np.max(data)+step, dtype=int)

def plot_on_bars(plt, bars):
    for bar, count in zip(bars[2], bars[0]):
        plt.text(bar.get_x() + bar.get_width()/2, count, int(count), ha='center', va='bottom')

def config_plot(plt, title, x_label, y_label):
    plt.grid(True)
    plt.tight_layout()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
