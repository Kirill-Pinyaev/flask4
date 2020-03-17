from flask import Flask
from temp.Tests_ex.web_9.tasks.no1_1.data import db_session
from temp.Tests_ex.web_9.tasks.no1_1.data.users import User
from temp.Tests_ex.web_9.tasks.no1_1.data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    # app.run()

    session = db_session.create_session()

    collaborations = {x.id: len(x.collaborators.split())
                      for x in session.query(Jobs).all()}

    max_size = max(collaborations.values())
    ids = [x for x in collaborations if collaborations[x] == max_size]

    teamleaders = session.query(User).filter(User.id.in_(ids))

    for member in teamleaders:
        print(member.name, member.surname)
    session.commit()


if __name__ == '__main__':
    main()
