import argparse

from dataset import get_dataset_type

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_type", default="", type=str)
    parser.add_argument("--train_set", default="", type=str)
    parser.add_argument("--test_set", default="", type=str)
    parser.add_argument("--shuffle", default=True, type=bool)
    args = parser.parse_args()

    DatasetT = get_dataset_type("amazon_grocery_and_gourmet_foods")
    train_set = DatasetT(args.train_set, shuffle=True)
    train_ratings = train_set.get_ratings()
    avg_train_rating = train_ratings.mean()

    test_set = DatasetT(args.test_set, shuffle=True)
    test_ratings = test_set.get_ratings()
    mse = ((test_ratings - avg_train_rating) ** 2).mean()
    print("mes: {}".format(mse))


if __name__ == "__main__":
    main()
