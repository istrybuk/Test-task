import pytest
import sqlite3 as sql
import random


def val_random_to_20():
    return random.randint(1, 20)


def val_random_to_200():
    return random.randint(1, 200)


name_db = f"{val_random_to_200()}.db"
print(f"Создана база данных: {name_db}", {name_db})


@pytest.fixture(scope="session", autouse=True)
def conn():
    """Подключение к БД перед тестами, отключение после."""
    db = sql.connect(name_db)
    print(f"Создана база данных:, db")

    cursor = db.cursor()

    yield db, cursor

    cursor.close()
    db.close()


@pytest.fixture(scope="function", autouse=True)
def add_database(conn):
    db = conn[0]
    cursor = conn[1]

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
    )"""
    cursor.executescript(query)

    """ Таблица Ships"""
    """Диапазон значений для параметров: 1-200"""
    for i in range(1, 201):
        name_ship = f"Ship-{i}"
        name_weapon = f"Weapon-{i}"
        name_hull = f"Hull-{i}"
        name_engine = f"Engine-{i}"
        cursor.execute("INSERT INTO Ships VALUES (?, ?, ?, ?)", (name_ship, name_weapon, name_hull, name_engine))

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

    """ Таблица engines"""
    """Диапазон значений для целочисленных параметров: 1-6"""
    for i in range(1, 7):
        engine_of_engines = f"Engine-{i}"
        vl_power = val_random_to_20()
        vl_type_of_engines = val_random_to_20()
        cursor.execute("INSERT INTO engines VALUES (?, ?, ?)", (
            engine_of_engines, vl_power, vl_type_of_engines))

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

    return cursor
#
def test_1(add_database):
    print("ok")
