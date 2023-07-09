from db_config import Users


def main():
    user_name = input("名前を入力してください > ")

    user_weight = input("体重を入力してください > ")

    Users.create(name=user_name, weight=user_weight)


if __name__ == "__main__":
    main()
