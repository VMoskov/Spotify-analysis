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


def miliseconds_to_seconds(data):
    data['duration_s'] = data['duration_ms'] / 1000
    return data


def seconds_to_mmss(data):
    data['duration_mm:ss'] = data['duration_s'].apply(lambda x: '{:01d}:{:02d}'.format(int(x // 60), int(x % 60)))
    return data


if __name__ == '__main__':
    data = get_data('../data/spotify_data.csv')
    if check_missing_values(data) > 0:
        data = data.dropna()
        assert check_missing_values(data) == 0


