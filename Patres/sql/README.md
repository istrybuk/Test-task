# Часть 4: Работа с базами данных (Демо-БД)

## Задача:
Используя демо-базу [sandbox](https://github.com/istrybuk/Test-task/tree/main/Patres/sql):

Напишите SQL-запрос, который выводит данные о пассажирах, участвующих в поездке с идентификатором
7771 (id, trip, passenger, place, name)

```SQL запрос```
```
SELECT PT.id, PT.trip, PT.passenger, PT.place, P.name  FROM Trip as T
LEFT JOIN Pass_in_trip as PT
ON T.id = PT.trip
LEFT JOIN Passenger as P
ON PT.passenger = P.id
WHERE T.id = 7771
```

![sql.jpg](https://github.com/istrybuk/Test-task/blob/main/Patres/sql/sql.jpg)
