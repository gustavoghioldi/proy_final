# metodos save(Product) y get_all
# metodos save(Client) y get_all
from services.abstract_service import AbstractService
from models.product import Product

class ProductService(AbstractService):
    def __init__(self):
        self._create_table_script = "CREATE TABLE product (name TEXT, price NUMERIC)"
    
    def save(self, product:Product)->bool:
        conn, cursor = self.connector()
        cursor.execute("INSERT INTO product (name, price) values (?, ?)", (product.name, product.price))
        conn.commit()
        conn.close()
        return True

    def get_all(self):
        conn, cursor = self.connector()
        cursor.execute("SELECT * FROM product")
        rta = cursor.fetchall()
        conn.close()
        return rta