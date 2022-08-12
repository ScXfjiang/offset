import argparse

import numpy as np

from dataset import AmazonElectronics
from dataset import AmazonVideoGames
from dataset import AmazonGourmetFoods


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="", type=str)
    parser.add_argument("--shuffle", default=True, type=bool)
    args = parser.parse_args()

    if args.dataset.endswith("reviews_Electronics_5.json"):
        Dataset = AmazonElectronics
    elif args.dataset.endswith("reviews_Video_Games_5.json"):
        Dataset = AmazonVideoGames
    elif args.dataset.endswith("reviews_Grocery_and_Gourmet_Food_5.json"):
        Dataset = AmazonGourmetFoods
    else:
        raise NotImplementedError

    dataset = Dataset(args.dataset, shuffle=True)
    ratings = dataset.get_ratings()

    # train(70%) / validation(10%) / test(20%)
    chunk_size = int(0.1 * ratings.shape[0])
    train_ratings = ratings[: 7 * chunk_size]
    test_ratings = ratings[-2 * chunk_size :]

    avg_train_rating = train_ratings.mean()
    mse = ((test_ratings - avg_train_rating) ** 2).mean()
    print("mes: {}".format(mse))


if __name__ == "__main__":
    main()
