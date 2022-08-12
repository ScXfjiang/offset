import json
import numpy as np
import random

# dataset_file = "/data/xuefei/amazon/reviews_Video_Games_5.json"
dataset_file = "/data/xuefei/amazon/reviews_Grocery_and_Gourmet_Food_5.json"

ratings = []
with open(dataset_file, "rb") as f:
    for line in f:
        js = json.loads(line)
        ratings.append(float(js["overall"]))
random.shuffle(ratings)
ratings = np.array(ratings)

train_size = int(0.8 * ratings.shape[0])
test_size = len(ratings) - train_size
train_ratings = ratings[:train_size]
test_ratings = ratings[-test_size:]

avg_rating = train_ratings.mean()
mse = 1/test_size * sum((test_ratings - avg_rating) ** 2)
print(mse)
