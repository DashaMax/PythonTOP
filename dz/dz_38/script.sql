CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE,
    author TEXT NOT NULL,
    publishing TEXT NOT NULL,
    year INTEGER NOT NULL,
    pages INTEGER NOT NULL,
    price INTEGER NOT NULL,
    image TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL UNIQUE
);

INSERT INTO menu
VALUES (NULL, 'Главная', '/'),
       (NULL, 'О нас', '/about'),
       (NULL, 'Добавить', '/add'),
       (NULL, 'Доставка', '/delivery'),
       (NULL, 'Контакты', '/contacts');