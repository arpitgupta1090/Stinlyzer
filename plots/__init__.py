import numpy as np
import random
import io
from matplotlib import pyplot as plt
import matplotlib
import colorsys
matplotlib.use('Agg')


def random_color():
    random_number = random.randint(0, 16777215)
    hex_number = format(random_number, 'x')
    hex_number = '#' + hex_number
    return hex_number


def get_hex_colors(N):
    hsv_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    rgv_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples)
    return rgv_tuples


def build_graph(x_coordinates, y_coordinates, split_neg=False):
    img = io.BytesIO()
    if split_neg:
        pos = np.flatnonzero(x_coordinates > 0)[0]
        plt.plot(x_coordinates[:pos], y_coordinates[:pos], color='b')
        plt.plot(x_coordinates[pos:], y_coordinates[pos:], color='b')
    else:
        plt.plot(x_coordinates, y_coordinates, color=(0.5, 0, 0.25))
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img


def build_pie(data, labels):
    img = io.BytesIO()
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(data, labels=labels, autopct='%1.2f%%')
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img


def build_bar(data, labels):
    img = io.BytesIO()
    plt.bar(labels, data, color='maroon',
            width=0.4)
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img


def build_multi_bar(labels, data, xlabel, ylabel):
    img = io.BytesIO()
    N = len(next(iter(data.values())))
    fig = plt.subplots(figsize=(12, 8))

    # set width of bar
    barWidth = 1 / (len(data.keys()) + 1)
    colors = list(get_hex_colors(N))
    br0 = np.arange(N)
    multiplier = 1
    for k, v in data.items():
        plt.bar(br0 + (barWidth * multiplier), v, color=colors[multiplier-1], width=barWidth, edgecolor='grey', label=k)
        multiplier += 1

    # Adding Xticks
    plt.xlabel(xlabel, fontweight='bold', fontsize=15)
    plt.ylabel(ylabel, fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(N)], labels)

    plt.legend()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img


def build_stacked_plot(data, labels, legends, xlabel, ylabel):
    img = io.BytesIO()
    N = len(data[0])

    ind = np.arange(N)  # the x locations for the groups
    width = 1 / (N + 1)
    fig = plt.subplots(figsize=(10, 7))
    plot_legend = list()
    colors = list(get_hex_colors(N))
    bottom = None
    for i in range(len(data)):
        if i > 0:
            if bottom is None:
                bottom = np.array(data[i-1])
            else:
                bottom = np.array(bottom) + np.array(data[i - 1])
        p = plt.bar(ind, data[i], width, bottom=bottom, color=colors[i])
        plot_legend.append(p[0])

    plt.ylabel(ylabel)
    plt.title(xlabel)
    plt.xticks(ind, labels)
    plt.legend(plot_legend, legends)

    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img
