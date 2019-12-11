
import dbhandler as db
database = r"c:\sqlite\db\pythonsqlite.db"

conn = db.create_connection(database)

db.create_table(conn)

num = 1
label = "boss"

data = (num, num, num, label)
db.insert_data(conn, data)
db.insert_data(conn, data)

conn.commit()

db.read_data(conn)

conn.close()
