DATA_PATH="/data/xuefei/dataset/amazon/amazon_apps_for_android"

python main.py --dataset_type="amazon_apps_for_android" \
    --train_set="${DATA_PATH}/train.json" \
    --test_set="${DATA_PATH}/test.json"
