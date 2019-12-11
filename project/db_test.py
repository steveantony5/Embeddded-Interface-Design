
import dbhandler as db
database = r"c:\sqlite\db\eidproject.db"

conn = db.create_connection(database)

db.create_table(conn)

#command = "correcto"
#label = "boss"

#data = (command, label)
#db.insert_data(conn, data)
#db.insert_data(conn, data)

#conn.commit()

db.read_data(conn)

conn.close()
