from flask import Flask, render_template, redirect
from temp.Tests_ex.web_9.tasks.no1_5.data import db_session
from temp.Tests_ex.web_9.tasks.no1_5.data.users import User
from temp.Tests_ex.web_9.tasks.no1_5.data.jobs import Jobs
from temp.Tests_ex.web_9.tasks.no1_5.data.departments import Department
from temp.Tests_ex.web_9.tasks.no1_5.data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()

    # department = Department()
    # department.title = "Department of transportation"
    # department.chief = 4
    # department.email = "transport@mars.org"
    # department.members = "26, 37, 19"

    # department = Department()
    # department.title = "Department of construction"
    # department.chief = 6
    # department.email = "build@mars.org"
    # department.members = "16, 17, 28"

    # department = Department()
    # department.title = "Department of of construction"
    # department.chief = 6
    # department.email = "build@mars.org"
    # department.members = "9, 13, 18"

    # department = Department()
    # department.title = "Department of biological research"
    # department.chief = 3
    # department.email = "bio@mars.org"
    # department.members = "7, 10, 11"

    # department = Department()
    # department.title = "Department of geological exploration"
    # department.chief = 2
    # department.email = "geo@mars.org"
    # department.members = "6, 8, 12"
    department = session.query(Department).filter(Department.id == 1).first()
    department.members = '3, 4, 5'
    # session.add(department)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
