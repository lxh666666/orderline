# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@81.70.149.29/food_db?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

APP = {
    # 'domain':'127.0.0.1:8000'
    'domain':'https://www.orderline.xyz'
}

RELEASE_VERSION="20180729001"