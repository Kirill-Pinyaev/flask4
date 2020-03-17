from flask import Flask, render_template
from temp.Tests_ex.web_9.tasks.no1_3.data import db_session
from temp.Tests_ex.web_9.tasks.no1_3.data.users import User
from temp.Tests_ex.web_9.tasks.no1_3.data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")

    session = db_session.create_session()

    @app.route("/")
    def index():
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        users = session.query(User).all()
        names = {name.id: (name.surname, name.name) for name in users}
        return render_template("index.html", jobs=jobs, names=names)

    app.run()


if __name__ == '__main__':
    main()
