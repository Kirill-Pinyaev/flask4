from flask import Flask, session

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    # user = User()
    # user.name = "Пользователь 25"
    # user.about = "биография пользователя 5"
    # user.email = "email25@email.ru"
    # user.set_password("dagdfagds")

    # session = db_session.create_session()
    # session.add(user)
    # session.commit()
    app.run()

    for user in session.query(User).filter((User.id > 1) | (User.email.like("%4%"))):
        print(user)


if __name__ == '__main__':
    main()