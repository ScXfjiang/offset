import json
import random
import numpy as np


def get_dataset_type(type):
    if type == "amazon_electronics":
        Dataset = AmazonElectronics
    elif type == "amazon_video_games":
        Dataset = AmazonVideoGames
    elif type == "amazon_grocery_and_gourmet_foods":
        Dataset = AmazonGroceryAndGourmetFoods
    else:
        raise NotImplementedError
    return Dataset


class DatasetIf(object):
    def __init__(self, path, shuffle):
        super().__init__()

    def get_ratings(self):
        raise NotImplementedError


class Amazon(DatasetIf):
    def __init__(self, path, shuffle=False):
        super().__init__(path, shuffle)
        self.ratings = []
        with open(path, "rb") as f:
            for line in f:
                js = json.loads(line)
                self.ratings.append(float(js["overall"]))
        if shuffle:
            random.shuffle(self.ratings)
        self.ratings = np.array(self.ratings)

    def get_ratings(self):
        return self.ratings


class AmazonElectronics(Amazon):
    def __init__(self, path, shuffle=False):
        super().__init__(path, shuffle)


class AmazonVideoGames(Amazon):
    def __init__(self, path, shuffle=False):
        super().__init__(path, shuffle)


class AmazonGroceryAndGourmetFoods(Amazon):
    def __init__(self, path, shuffle=False):
        super().__init__(path, shuffle)
