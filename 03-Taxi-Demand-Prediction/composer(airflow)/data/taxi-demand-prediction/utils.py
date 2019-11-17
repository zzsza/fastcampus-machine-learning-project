import os
import yaml
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './'))


def init_config(dev_env):
    bigquery_config = yaml.load(
        open(
            os.path.join(root_path, 'config.yaml'),
            'r'
        )
    )

    return bigquery_config[dev_env]


def split_train_and_test(df, date):
    """
    Dataframe에서 train_df, test_df로 나눠주는 함수

    df : 시계열 데이터 프레임
    date : 기준점 날짜
    """
    train_df = df[df['pickup_hour'] < date]
    test_df = df[df['pickup_hour'] >= date]
    return train_df, test_df


def load_model(file_path):
    model = joblib.load(open(file_path, 'rb'))
    return model


def evaluation(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    score = pd.DataFrame([mape, mae, mse], index=['mape', 'mae', 'mse'], columns=['score']).T
    return score
