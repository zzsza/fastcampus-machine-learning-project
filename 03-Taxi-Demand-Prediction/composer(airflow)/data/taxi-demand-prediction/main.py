import argparse
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import rf_trainer
from base_data import base_query
from utils import init_config, split_train_and_test

parser = argparse.ArgumentParser()

parser.add_argument("--dev_env", help="Development Env [local], [development], [production]", type=str, default="local")
parser.add_argument("--mode", help="[train], [predict]", type=str, default='predict')

flag = parser.parse_args()

# init config(개발 환경, train, predict 등)
config = init_config(flag.dev_env)
print(config)
model_dir = f"{config['save_folder']}/models/"

# Feature Engineering(using BigQuery)
print('load data')
base_df = pd.read_gbq(query=base_query, dialect='standard', project_id=config['project'])

# Data Preprocessing(Label Encoding)
zip_code_le = LabelEncoder()
base_df['zip_code_le'] = zip_code_le.fit_transform(base_df['zip_code'])

# Split Train and Test Data
# 지금은 고정값을 기준으로 Train / Test를 나누지만 실전에선 이 부분이 동적으로 설정되야 함(2015-01-24이 아닌)
train_df, test_df = split_train_and_test(base_df, '2015-01-24')
print('data split end')

del train_df['zip_code']
del train_df['pickup_hour']
del test_df['zip_code']
del test_df['pickup_hour']

y_train_raw = train_df.pop('cnt')
y_test_raw = test_df.pop('cnt')

train_df = train_df.fillna(method='backfill')
test_df = test_df.fillna(method='backfill')

x_train = train_df.copy()
x_test = test_df.copy()

if __name__ == '__main__':
    if not os.path.isdir(model_dir):
        os.mkdir(model_dir)
    if flag.mode == 'train':
        print('train start')
        train_op = rf_trainer.Trainer(config)
        train_op.train(x_train, y_train_raw)

    elif flag.mode == 'predict':
        print('predict start')
        train_op = rf_trainer.Trainer(config)
        train_op.predict(x_test, y_test_raw)
    else:
        raise KeyError(f"Incorrect value flag.mode = {flag.mode}")
