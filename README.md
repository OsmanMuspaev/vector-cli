# Vector Editor CLI

Простой **командный редактор векторных фигур** на Python.  
Поддерживает базовые геометрические объекты и операции с ними через терминал/консоль.

---

## Поддерживаемые фигуры

| Фигура  | Параметры | Пример создания |
|---------|-----------|----------------|
| Point   | x, y      | `create point 1 2` |
| Segment | x1, y1, x2, y2 | `create segment 0 0 5 5` |
| Circle  | x, y, r   | `create circle 0 0 5` |
| Square  | x, y, size | `create square 1 1 10` |

---

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/OsmanMuspaev/vector-cli
cd vector_editor
```

2. Убедиться, что установлен Python 3.8+

3. Запустить программу:

```bash
python main.py
```

---

## Доступные команды

| Команда  | Описание |
|---------|-----------|
| Point   | Создать фигуру (см. таблицу выше) |
| list | Показать все фигуры в виде таблицы с ID, TYPE, DATA |
| update <id> <parameters>  | Изменить фигуру по ID |
| delete <id>  | Удалить фигуру по ID |
| clear | Удалить все фигуры |
| info <id> | Показать подробную информацию о фигуре |
| help | Показать этот список команд |
| exit | Выйти из программы |

---

## Архитектура проекта

```
vector_editor/
│
├── main.py           # CLI и обработка команд
├── factory.py        # ShapeFactory для создания фигур
└── shapes/
    ├── __init__.py
    ├── shape.py      # базовый абстрактный класс Shape
    ├── point.py
    ├── segment.py
    ├── circle.py
    └── square.py
```
