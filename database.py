import sqlite3
#my db
create_beans_table='create table if not exists beans(id integer primary key,name text not null,method text not null,rating integer not null)'
insert_beans="insert into beans(name,method,rating) values(%s,%s,%s);"
get_all_Beans="select * from beans order by rating desc" #limit 1;
beans_by_name='select * from beans where name=?;'
get_best_preparation_for_beans="""select * from beans where name=?
                                  order by rating desc
                                  limit 1;
                                """

def connect():
    return sqlite3.connect('data.db')

def create_tables(connection):

    with connection:
        try:
            connection.execute(create_beans_table)
        except OperationalError as o:
            print(o)

def add_bean(connection,name,method,rating):
    with connection:
        connection.execute(insert_beans,(name,method,rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(get_all_Beans).fetchall()

def get_beans_by_name(connection,name):
    with connection:
        return connection.execute(beans_by_name,(name,)).fetchall()

def get_best_prep_for_bean(connection,name):
    with connection:
        return connection.execute(get_best_preparation_for_beans,(name,)).fetchone()