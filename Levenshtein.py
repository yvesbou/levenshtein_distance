

def Levenshtein_distance(a, b):
    """
    Recursively computes the Levenshtein distance between string a and b
    :return: Levenshtein distance between a and b
    """
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return Levenshtein_distance(a[1:], b[1:])
    else:
        return 1 + min(Levenshtein_distance(a[1:], b), Levenshtein_distance(a, b[1:]), Levenshtein_distance(a[1:], b[1:]))


def Levenshtein(data):
    """
    :param data: pd.dataframe which has column 'HUNDENAME'
    :return: dataframe with a new column that contains the Levenshtein distance to Luca for each name
    """
    data["Levenshtein_distance_toLuca"] = data['HUNDENAME'].apply(lambda x: Levenshtein_distance(x, 'Luca'))
    return data