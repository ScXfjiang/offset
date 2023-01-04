import argparse

from dataset import get_dataset_type

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_type", default="", type=str)
    parser.add_argument("--train_set", default="", type=str)
    parser.add_argument("--test_set", default="", type=str)
    args = parser.parse_args()

    DatasetT = get_dataset_type(args.dataset_type)
    train_set = DatasetT(args.train_set)
    train_ratings = train_set.get_ratings()
    avg_train_rating = train_ratings.mean()

    test_set = DatasetT(args.test_set)
    test_ratings = test_set.get_ratings()
    mse = ((test_ratings - avg_train_rating) ** 2).mean()
    print("mes: {}".format(mse))


if __name__ == "__main__":
    main()
