from jinja2 import Environment, FileSystemLoader


def main():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    text = {
        'title': 'Домашнее задание',
        'textH': 'Страница с домашним заданием',
        'textP': 'Домашнее задание выполнено!!!'
    }

    tm = env.get_template('index.html')
    msg = tm.render(title=text['title'], textH=text['textH'], textP=text['textP'])

    with open('homework.html', 'w') as file:
        file.write(msg)


if __name__ == '__main__':
    main()