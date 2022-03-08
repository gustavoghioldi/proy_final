import sqlite3

class AbstractService:
    def __init__(self):
        # var example: "CREATE TABLE client (name TEXT, dni NUMERIC)"
        self._create_table_script = "" 
           
    def connector(self):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        try:
            cursor.execute(self._create_table_script)
        except sqlite3.OperationalError:
            pass
        return conn, cursor