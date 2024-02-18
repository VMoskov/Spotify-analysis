import matplotlib.pyplot as plt
from IPython import get_ipython
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


def top_tracks_per_genre(genre_name, number_of_tracks):
    dataset = get_ipython().user_ns['dataset']

    tracks = dataset[dataset['genre'] == genre_name].sort_values('popularity', ascending=False).head(number_of_tracks)
    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='popularity', y='track_name', data=tracks, palette='viridis')
    plt.title(f'Top {number_of_tracks} {genre_name} tracks')
    plt.xlabel('Popularity')
    plt.ylabel('Track Name')
    plt.show()


def top_tracks_per_artist(artist_name, number_of_tracks):
    dataset = get_ipython().user_ns['dataset']

    tracks = dataset[dataset['artist_name'] == artist_name].sort_values('popularity', ascending=False).head(number_of_tracks)
    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='popularity', y='track_name', data=tracks, palette='viridis')
    plt.title(f'Top {number_of_tracks} {artist_name} tracks')
    plt.xlabel('Popularity')
    plt.ylabel('Track Name')
    plt.show()