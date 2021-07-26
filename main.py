import pandas as pd
from Levenshtein import Levenshtein

url = "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv"


def download_to_df(url):
    """
    :param url: url to a csv (string)
    :return: pandas dataframe
    """
    dog_data = pd.read_csv(url)
    return dog_data


def requirement(data):
    """
    :param data: dataframe that contains information about the Levenshtein distance to 'Luca' for each row
    :return: returns pandas series that provides all the names that fulfill condition
    """
    selection = data[data["Levenshtein_distance_toLuca"].eq(1)]
    return selection['HUNDENAME']


def output(names):
    """
    :param names: iterable/pd.series that contains strings
    :return: string with format "name1, name2, name3, ..."
    """
    out = ""
    names = set(names)
    length = len(names)
    for i, name in enumerate(names):
        if i+1 == length:
            out += name
        else:
            out += name + ", "
    return out


if __name__ == '__main__':
    dog_data = download_to_df(url)
    updated_dog_data = Levenshtein(dog_data)
    designated_dog_names = requirement(updated_dog_data)
    print(output(designated_dog_names))

