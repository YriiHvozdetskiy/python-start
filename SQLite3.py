import sqlite3

DB_NAME = 'sqlite_db.db'

with sqlite3.connect(DB_NAME) as sqlite_connection:
    sql_request = "SELECT * FROM courses WHERE reviesws_qty>= 30"
    sql_cursor = sqlite_connection.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)

# Add recordds to the courses table
# courses = [
#     (351, 'JavaScript course', 415, 100),
#     (614, 'C++ course', 161, 10),
#     (721, 'Java full course', 100, 35)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_connection:
#     sqlite_request = "INSERT INTO courses VALUES(?,?,?,?)"
#     # sqlite_connection.execute(sqlite_request, (251, 'Python course', 100, 30))
#     for course in courses:
#         sqlite_connection.execute(sqlite_request, course)
#     sqlite_connection.commit() # - зберігаєм дані в базі

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_connection:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#      id integer PRIMARY KEY,
#      title text NOT NULL,
#      students_qty integer,
#      reviesws_qty integer
#      ); """
#     sqlite_connection.execute(sql_request)
