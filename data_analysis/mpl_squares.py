import matplotlib.pyplot as plt
import numpy as np

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plot_style_list = [
                   'Solarize_Light2', '_classic_test_patch', 'bmh',
                   'classic', 'dark_background', 'fast', 'fivethirtyeight',
                   'ggplot', 'grayscale', 'seaborn', 'seaborn-bright',
                   'seaborn-colorblind', 'seaborn-dark',
                   'seaborn-dark-palette', 'seaborn-darkgrid',
                   'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
                   'seaborn-paper', 'seaborn-pastel', 'seaborn-poster',
                   'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
                   'seaborn-whitegrid', 'tableau-colorblind10'
                   ]

for plot_style in plot_style_list:
    if plot_style == 'tableau-colorblind10':
        plt.style.use(plot_style)
        fig, ax = plt.subplots()
        ax.plot(input_values, squares, linewidth=3)

        # Set chart title and label axis.
        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        # Set size of tick labels.
        ax.tick_params(axis='both', labelsize=14)

        plt.show()
