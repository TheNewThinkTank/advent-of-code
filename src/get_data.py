

def get_data(datafile: str) -> list[str]:
    """_summary_

    :param datafile: _description_
    :type datafile: str
    :return: _description_
    :rtype: list[str]
    """

    with open(datafile, "r") as rf:
        lines = rf.readlines()

    return [line.removesuffix("\n") for line in lines]


def get_all_data(datafile: str):
    with open(datafile, "r") as f:
        data = f.read()
    return data
