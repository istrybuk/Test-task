
def test_sqlite_one(update_database):
    cursor, new_db = update_database
    data = new_db.execute("SELECT * FROM hulls").fetchall()
    print(f'\n До изменений: {data[:3]}')
    da3ta = cursor.execute("SELECT * FROM hulls").fetchall()
    print(f'\n После изменений:  {da3ta[:3]}')
    print('Ok')


def test_sqlite_two(update_database):
    pass
