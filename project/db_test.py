
import dbhandler as db

conn = db.create_connection()

db.create_table(conn)

num = 1
label = "boss"

data = (num, num, num, num, label)
db.insert_data(conn, data)

db.read_data(conn)
