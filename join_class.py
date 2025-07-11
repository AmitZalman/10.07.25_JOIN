
import sqlite3
import os

conn = sqlite3.connect('10.07.25_Class')

# allow usage of column name, i.e. row['age']
conn.row_factory = sqlite3.Row  # ...magic ...

# create in memory
# erase after program exit
# conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

#Inner join

print('''
SELECT p.* , t.driver_name , t.car_type FROM  passengers p   
inner join taxis t on p.taxi_id = t.id;
''')

cursor.execute('''
SELECT p.* , t.driver_name , t.car_type FROM  passengers p   
inner join taxis t on p.taxi_id = t.id;
''')

result = cursor.fetchall()
for row in result:
    print(dict(row))


#left join
print('-' * 100)

print('''
SELECT p.* , t.driver_name , t.car_type FROM  passengers p   
left join taxis t on p.taxi_id = t.id;
''')

cursor.execute('''
SELECT p.* , t.driver_name , t.car_type FROM  passengers p   
left join taxis t on p.taxi_id = t.id;
''')

result = cursor.fetchall()
for row in result:
    print(dict(row))

#outer join
print('-' * 100)


print('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
left join taxis t on p.taxi_id = t.id
WHERE taxi_id IS NOT NULL;
''')


cursor.execute('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
left join taxis t on p.taxi_id = t.id
WHERE taxi_id IS NULL;
''')

result = cursor.fetchall()
for row in result:
    print(dict(row))


#FULL join
print('-' * 100)
print('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
FULL JOIN taxis t on p.taxi_id = t.id;\n''')


cursor.execute('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
FULL JOIN taxis t on p.taxi_id = t.id;
''')

result = cursor.fetchall()
for row in result:
    print(dict(row))

#CROSS join
print('-' * 100)
print('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
CROSS JOIN taxis t on p.taxi_id = t.id;\n
''')


cursor.execute('''
SELECT p.* , t.driver_name , t.car_type FROM passengers p
CROSS JOIN taxis t;
''')

result = cursor.fetchall()
for row in result:
    print(dict(row))

conn.commit()  # write changes

conn.close()  # close for safety