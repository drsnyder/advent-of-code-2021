import os


def load_data_file(day, part):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f"../data/day-{day}-{part}.txt")
    with open(filename) as f:
        data = [line.strip() for line in f]

    return data
