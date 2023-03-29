# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 22:45
# @Author  : dfz
# @FileName: user.py
# @Software: PyCharm
from apps.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)