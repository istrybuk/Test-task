# import pytest
import sqlite3 as sql
import random


def val_random_to_20():
    return random.randint(1, 20)


def val_random_to_200():
    return random.randint(1, 200)


name_db = f"{val_random_to_200()}.db"
print(name_db)

# @pytest.fixture(scope="session")
# def connection():
#     """Подключение к БД перед тестами, отключение после."""
#     db = sql.connect(name_db)
#     cursor = db.cursor()
#     yield db, cursor
#     cursor.close()
#     db.close()


def add_database():
    db = sql.connect(name_db)
    cursor = db.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS Ships(
        ship TEXT PRIMARY KEY,
        weapon TEXT,
        hull TEXT,
        engine TEXT
    );
    CREATE TABLE IF NOT EXISTS weapons(
        weapon TEXT PRIMARY KEY,
        reload_speed INTEGER,
        rotational_speed INTEGER,
        diameter INTEGER,
        power_volley INTEGER,
        count INTEGER,
        FOREIGN KEY (weapon) REFERENCES Ships(weapon)
    );
    CREATE TABLE IF NOT EXISTS engines(
        engine TEXT PRIMARY KEY,
        power INTEGER NOT NULL,
        type INTEGER NOT NULL,
        FOREIGN KEY (engine) REFERENCES Ships(engine)
    );
    CREATE TABLE IF NOT EXISTS hulls(
    hull TEXT PRIMARY KEY,
    armor INTEGER NOT NULL,
    type INTEGER NOT NULL,
    capacity INTEGER NOT NULL,
    FOREIGN KEY (hull) REFERENCES Ships(hull)
    )
    """
    cursor.executescript(query)

    """ Таблица Ships"""
    """Диапазон значений для параметров: 1-200"""
    for i in range(1, 201):
        name_ship = f"Ship-{i}"
        name_weapon = f"Weapon-{i}"
        name_hull = f"Hull-{i}"
        name_engine = f"Engine-{i}"
        cursor.execute("INSERT INTO Ships VALUES (?, ?, ?, ?)", (name_ship, name_weapon, name_hull, name_engine))
        db.commit()

    """ Таблица weapons"""
    """Диапазон значений для целочисленных параметров: 1-20"""
    for i in range(1, 21):
        weapon_of_weapons = f"Weapon-{i}"
        vl_reload_speed = val_random_to_20()
        vl_rotational_speed = val_random_to_20()
        vl_diameter = val_random_to_20()
        vl_power_volley = val_random_to_20()
        vl_count = val_random_to_20()
        cursor.execute("INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?)", (
            weapon_of_weapons, vl_reload_speed, vl_rotational_speed, vl_diameter, vl_power_volley, vl_count))
        db.commit()

    """ Таблица engines"""
    """Диапазон значений для целочисленных параметров: 1-6"""
    for i in range(1, 7):
        engine_of_engines = f"Engine-{i}"
        vl_power = val_random_to_20()
        vl_type_of_engines = val_random_to_20()
        cursor.execute("INSERT INTO engines VALUES (?, ?, ?)", (
            engine_of_engines, vl_power, vl_type_of_engines))
        db.commit()

    """ Таблица hulls"""
    """Диапазон значений для целочисленных параметров: 1-5"""
    for i in range(1, 6):
        hull_of_hulls = f"Hull-{i}"
        vl_armor = val_random_to_20()
        vl_type_of_hulls = val_random_to_20()
        vl_capacity = val_random_to_20()
        cursor.execute("INSERT INTO hulls VALUES (?, ?, ?, ?)", (
            hull_of_hulls, vl_armor, vl_type_of_hulls, vl_capacity))
        db.commit()
    cursor.close()
    db.close()

# @pytest.mark.parametrize("table_name", ["weapons", "hulls", "engines"])
# def test_component_changes(connection, table_name):


def update_random_value():
    db = sql.connect(name_db)
    memory_db = sql.connect(':memory:')
    db.backup(memory_db)
    cursor = memory_db.cursor()

    """ Таблица Ships"""
    """Диапазон значений для параметров: 1-200"""
    # база до изменения
    data = cursor.execute("SELECT * FROM Ships").fetchall()
    print(data[:3])

    # список названий колонок
    names_s = list(map(lambda x: x[0], cursor.description))
    first_names, random_other_name = names_s[0], random.choice(names_s[1:])

    # выборка случайной колонки
    data_select_column = cursor.execute(f"SELECT {random_other_name} FROM Ships").fetchall()

    """Проходимся по всей таблице, в случайной колонке,
     изменяем значение после “-” на случайное по условию"""
    for vl in data:
        first_col = vl[0]
        for el in data_select_column:
            column_value = el[0].split('-')
            new_value = f"{column_value[0]}-{val_random_to_200()}"
            cursor.execute(f"UPDATE Ships SET {random_other_name} = '{new_value}' WHERE {first_names} = '{first_col}'")
            memory_db.commit()
    data = cursor.execute("SELECT * FROM Ships").fetchall()
    print(data[:3])

    """ Таблица hulls"""
    """Диапазон значений для целочисленных параметров: 1-20"""
    original_ship = cursor.execute("SELECT * FROM hulls").fetchall()
    print(original_ship)
    random_name_colum = random.choice([description[0] for description in cursor.description][1:])
    for one_col in original_ship:
        new_name = one_col[0]
        cursor.execute(f"UPDATE hulls SET {random_name_colum} = {val_random_to_20()} WHERE hull = '{new_name}'")
        memory_db.commit()
    modified_ship = cursor.execute("SELECT * FROM hulls").fetchall()
    print(modified_ship)

    """ Таблица engines"""
    """Диапазон значений для целочисленных параметров: 1-20"""
    original_ship = cursor.execute("SELECT * FROM engines").fetchall()
    random_name_colum = random.choice([description[0] for description in cursor.description][1:])
    for one_col in original_ship:
        new_name = one_col[0]
        cursor.execute(f"UPDATE engines SET {random_name_colum} = {val_random_to_20()} WHERE engine = '{new_name}'")
        memory_db.commit()
    # modified_ship = cursor.execute("SELECT * FROM engines").fetchall()

    """ Таблица weapons"""
    """Диапазон значений для целочисленных параметров: 1-20"""
    original_ship = cursor.execute("SELECT * FROM weapons").fetchall()
    random_name_colum = random.choice([description[0] for description in cursor.description][1:])
    for one_col in original_ship:
        new_name = one_col[0]
        cursor.execute(f"UPDATE weapons SET {random_name_colum} = {val_random_to_20()} WHERE weapon = '{new_name}'")
        memory_db.commit()
    # modified_ship = cursor.execute("SELECT * FROM weapons").fetchall()
    # assert original_ship == modified_ship

    cursor.close()
    memory_db.close()
    db.close()


add_database()
update_random_value()
