from services.abstract_service import AbstractService
from models.sale import Sale
from services.dolar_service import DolarService
class SaleService(AbstractService):
    def __init__(self):
        self._create_table_script = "CREATE TABLE sale (product_name TEXT, product_price NUMERIC, client_dni TEXT, qty NUMERIC, total_price NUMERIC, total_price_usd NUMERIC)"
    
    def save(self, sale:Sale)->bool:
        conn, cursor = self.connector()
        total_price = sale.product_price * sale.qty
        total_price_usd = total_price/DolarService.get_usd_ccl()
        cursor.execute("INSERT INTO sale (product_name, product_price, client_dni, qty, total_price, total_price_usd) values (?, ?, ?, ?, ?, ?)", 
            (sale.product_name, sale.product_price, sale.client_dni, sale.qty, total_price, total_price_usd) )
        conn.commit()
        conn.close()
        return True
    
    def get_all(self):
        conn, cursor = self.connector()
        cursor.execute("SELECT * FROM sale")
        rta = cursor.fetchall()
        conn.close()
        return rta