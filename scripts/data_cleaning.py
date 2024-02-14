import pandas as pd


def get_data(path):
    missing_values = ['n/a', 'na', '--', ' ', 'N/A', 'NA', 'nan', 'NaN', 'NAN']
    return pd.read_csv(path, na_values=missing_values)


def clean_data(data):
    data = data.dropna().drop('Unnamed: 0', axis=1)
    return data[(data['loudness'] <= 0) & (data['time_signature'] >= 3)]


def check_missing_values(data):
    missing_values = data.isna().sum().sum()
    if missing_values > 0:
        print(f'There are {missing_values} missing values in the dataset')
    else:
        print('No missing values in the dataset')
    return missing_values


if __name__ == '__main__':
    data = get_data('../data/spotify_data.csv')
    if check_missing_values(data) > 0:
        data = data.dropna()
        assert check_missing_values(data) == 0


