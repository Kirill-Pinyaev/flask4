from flask import Flask
from temp.Tests_ex.web_9.tasks.no1_2.data import db_session
from temp.Tests_ex.web_9.tasks.no1_2.data.users import User
from temp.Tests_ex.web_9.tasks.no1_2.data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    # app.run()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"

    # user = User()
    # user.surname = "Watny"
    # user.name = "Mark"
    # user.age = 25
    # user.position = "middle scientist"
    # user.speciality = "biologist"
    # user.address = "module_2"
    # user.email = "mark@mars.org"
    # user.hashed_password = "bio"

    session = db_session.create_session()
    session.add(user)

    # for user in session.query(User).all():
    #     print(user)
    session.commit()

if __name__ == '__main__':
    main()
