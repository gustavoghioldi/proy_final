import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from models.client import Client
from models.product import Product
from models.sale import Sale
from services.sale_service import SaleService
from services.client_service import ClientService
from services.product_service import ProductService
from services.inform_service import InformService
## variables globales
products = []
clients = []
client_service = ClientService()
product_service = ProductService()
sale_service = SaleService()

clients = client_service.get_all()
print(clients)
products = product_service.get_all()
print(products)

def add_client():
    try:    
        client = Client(entry_client_name.get(), entry_client_dni.get())
        print(client.__dict__)    
        if client.name=="" or client.dni=="":
            raise Exception("client empty")
        if client_service.save(client):
            print("client save ok")
            #combo_clients.insert(tk.END, f"{client.name} {client.dni}")
            messagebox.showinfo(title="client", message="Ok!")
    except Exception:
        messagebox.showerror(title="error client", message="Error Save")

def add_product():
    try:
        product = Product(entry_product_name.get(), entry_product_price.get())
        print(product.__dict__)
        if product.name=="" or product.price=="":
            raise Exception("product empty")
        if product_service.save(product):
            print("product save ok")
            #combo_products.insert(tk.END, f"{product.name} {product.price}")
            messagebox.showinfo(title="product", message="Ok!")
    except Exception:
        messagebox.showerror(title="error product", message="Error Save")

def add_sale():
    try:    
        c_name, c_dni = combo_clients.get().split()
        p_name, p_price = combo_products.get().split()
        sale = Sale(Product(p_name, float(p_price)), Client(c_name, c_dni), int(entity_sale_qty.get()))
    
        if sale_service.save(sale):
            print("sale save")
            messagebox.showinfo(title="sale", message="Ok!")
    except Exception:
        messagebox.showerror(title="error sale", message="Error Save")
def create_inform():
    InformService.create_sales_report()


window = tk.Tk()
### client #######
label_client_name = tk.Label(text="Name:")
label_client_dni = tk.Label(text="DNI:")

label_client_name.place(x=10, y=50)
label_client_dni.place(x=310, y=50)

entry_client_name = tk.Entry()
entry_client_dni = tk.Entry()
entry_client_name.place(x=110, y=50)
entry_client_dni.place(x=410, y=50)

btn_create_client = tk.Button(text="Crear Cliente", command=add_client, width=20)
btn_create_client.place(x=240, y=100)
### end client ###

### product ######
label_product_name = tk.Label(text="Name:")
label_product_price = tk.Label(text="price:")
label_product_name.place(x=10, y=200)
label_product_price.place(x=310, y=200)

entry_product_name = tk.Entry()
entry_product_price = tk.Entry()
entry_product_name.place(x=110, y=200)
entry_product_price.place(x=410, y=200)

btn_create_product = tk.Button(text="Crear Product", command=add_product, width=20)
btn_create_product.place(x=240, y=250)
### end product ##

### sales ########
combo_clients = Combobox(
    values = clients
)
combo_products = Combobox(
    values = products
)
entity_sale_qty = tk.Entry()

combo_clients.place(x=10, y=400)
combo_products.place(x=210, y=400)

entity_sale_qty.place(x=410, y=400)
label_client = tk.Label(text="client:")
label_product = tk.Label(text="product:")
label_qty = tk.Label(text="Qty:")
label_client.place(x=10, y=350)
label_product.place(x=210, y=350)
label_qty.place(x=410, y=350)
btn_create_sale = tk.Button(text="Crear Venta", command=add_sale, width=20)
btn_create_sale.place(x=240, y=450)
### end sale #####

btn_create_inform = tk.Button(text="Create Report", command=create_inform, width=20)
btn_create_inform.place(x=240, y=550)
window.title("Sale System")
window.config(width=700, height=600)
window.mainloop()