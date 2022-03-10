# metodos save(Client) y get_all
from services.abstract_service import AbstractService
from models.client import Client

class ClientService(AbstractService):
    def __init__(self):
        self._create_table_script = "CREATE TABLE client (name TEXT, dni NUMERIC)"
    
    def save(self, client:Client)->bool:
        conn, cursor = self.connector()
        cursor.execute("INSERT INTO client (name, dni) values (?, ?)", (client.name, client.dni))
        conn.commit()
        conn.close()
        return True
    
    def get_all(self):
        conn, cursor = self.connector()
        cursor.execute("SELECT * FROM client")
        rta = cursor.fetchall()
        conn.close()
        return rta