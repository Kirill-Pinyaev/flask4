from flask import Flask
from temp.Tests_ex.web_9.tasks.no1_5.data import db_session
from temp.Tests_ex.web_9.tasks.no1_5.data.users import User
from temp.Tests_ex.web_9.tasks.no1_5.data.jobs import Jobs
from temp.Tests_ex.web_9.tasks.no1_5.data.departments import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()

    result = []
    work_hours = {}
    department = session.query(Department).filter(Department.id == 1).first()
    for lst in department.members.split(', '):
        arr = list(map(int, lst))  # list of member`s ids (integers)
        for num in arr:
            for job in session.query(Jobs).all():
                if num in [int(x) for x in job.collaborators.split(', ')]:
                    work_hours[num] = work_hours.get(num, 0) + job.work_size
            # print(work_hours)
            if work_hours[num] > 25:
                result.append(num)
    # print(result)

    for user in session.query(User).all():
        if user.id in result:
            print(user.surname, user.name)

    session.commit()


if __name__ == '__main__':
    main()
