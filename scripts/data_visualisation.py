import matplotlib.pyplot as plt
import seaborn as sns


def create_sample(dataset, percentage):
    return dataset.sample(frac=percentage, random_state=1)


def plot_data(dataset, x, y, hue):
    sns.scatterplot(x=x, y=y, data=dataset, hue=hue, palette='viridis', edgecolor='none')
    sns.regplot(x=x, y=y, data=dataset, scatter=False, color='r')
    plt.title(f'{x[0].upper() + x[1:]} vs {y[0].upper() + y[1:]}')
    plt.xlabel(x[0].upper() + x[1:])
    plt.ylabel(y[0].upper() + y[1:])
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
