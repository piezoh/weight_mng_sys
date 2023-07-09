import os
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, CharField, IntegerField

# .envの読み込み
load_dotenv()


# データベースへの接続設定
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合


# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


# 体重管理のモデル
class Users(Model):
    """Weight_MNG Model"""

    name = CharField()
    weight = IntegerField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([Users])
