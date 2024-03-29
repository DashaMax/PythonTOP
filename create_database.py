from faker import Faker

from models.database import create_db, Session
from models.lesson import Lesson
from models.student import Student
from models.group import Group


def create_database(load_fake_data=True):
    create_db()

    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons_names = ['Math', 'Programming', 'Algorithms', 'Physics']
    group1 = Group(group_name='MDA-7')
    group2 = Group(group_name='MDA-9')
    session.add(group1)
    session.add(group2)

    for key, item in enumerate(lessons_names):
        lesson = Lesson(lesson_title=item)
        lesson.groups.append(group1)

        if key % 2 == 0:
            lesson.groups.append(group2)

        session.add(lesson)

    faker = Faker(locale='ru_Ru')
    group_list = [group1, group2]
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        surname = full_name[0]
        name = full_name[1]
        patronymic = full_name[2]
        age = faker.random.randint(16, 25)
        group = faker.random.choice(group_list)
        student = Student(surname, name, patronymic, age, group.id)
        session.add(student)

    session.commit()
    session.close()