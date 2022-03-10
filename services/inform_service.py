from services.sale_service import SaleService

class InformService:
    
    @staticmethod
    def create_sales_report()->None:
        sale_services = SaleService()
        sales = sale_services.get_all()
        with open("informe.csv", "w") as f:
            for sale in sales:
                f.write(f"{sale[0]};{sale[1]};{sale[2]};{sale[3]};{sale[4]};{sale[5]}\n")

