from flask import Flask
from temp.Tests_ex.web_9.tasks.no1_1.data import db_session
from temp.Tests_ex.web_9.tasks.no1_1.data.users import User
from temp.Tests_ex.web_9.tasks.no1_1.data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_3.sqlite")
    # app.run()

    session = db_session.create_session()

    for user in session.query(User).filter(User.age < 18):
        print(f"{user} {user.age} years")
    session.commit()


if __name__ == '__main__':
    main()
