DATA_PATH="/data/xuefei/dataset/amazon/amazon_grocery_and_gourmet_foods1"

python main.py --dataset_type="amazon_grocery_and_gourmet_foods" \
    --train_set="${DATA_PATH}/train.json" \
    --test_set="${DATA_PATH}/test.json"
