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

    for job in session.query(Jobs).filter((Jobs.work_size < 20),
                                          Jobs.is_finished == 0):
        print(job)
    session.commit()


if __name__ == '__main__':
    main()
