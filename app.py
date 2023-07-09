from db_config import Users


def input_data():
    user_name = input("名前を入力してください > ")

    user_weight = input("体重を入力してください > ")

    Users.create(name=user_name, weight=user_weight)


def display_data():
    for usr in Users.select():
        print(usr.id, usr.name, usr.weight)


def main():
    print("入力:1,表示:2,終了:3 ")

    while True:
        select_num = int(input("必要な処理の番号を入力してください > "))

        if select_num == 1:
            input_data()
        elif select_num == 2:
            display_data()
        elif select_num == 3:
            print("処理終了")
            break
        else:
            print("1~3の番号を選んで入力してください")
            break


if __name__ == "__main__":
    main()
