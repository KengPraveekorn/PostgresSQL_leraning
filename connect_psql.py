import psycopg2 as psg
import pandas as pd

con = psg.connect(
    host='localhost',
    database='faculty',
    user='postgres',
    password='Admin!@#'
)

print(con)

# cursor -> ตัวที่ใช้ติดต่อกับ DB
cur = con.cursor()

# cur.execute('select * from employee')
# print(cur.fetchall())

# cur.execute('create table team(id_team serial primary key, team varchar, game varchar)')
# cur.execute('insert into team(team, game) values(%s,%s)',('Jackets','Rex'))
# cur.execute('select * from team')
# print(cur.fetchall())

# team =[
#     ('United','Asaurus'),
#     ('Athletic','Uber'),
#     ('Legs','Disguised'),
# ]
# for t in team:
#     cur.execute('insert into team(team, game) values (%s,%s)',t)
# cur.execute('select * from team')
# print(cur.fetchall())

df = pd.read_sql('select * from team',con)
print(df)

con.commit()
cur.close()
con.close()