import tkinter as tk
from tkinter.ttk import Combobox

## variables globales
products = []
clients = []

def setup():
    pass

def add_client():
    pass

def add_product():
    pass

def add_sale():
    pass

def create_inform():
    pass


window = tk.Tk()
### client #######
label_client_name = tk.Label(text="Name:")
label_client_dni = tk.Label(text="DNI:")
entry_client_name = tk.Entry()
entry_client_dni = tk.Entry()
btn_create_client = tk.Button(text="Crear Cliente", command=add_client, width=20)
label_client_name.place(x=10, y=50)
label_client_dni.place(x=10, y=150)
entry_client_name.place(x=200, y=50)
entry_client_dni.place(x=200, y=150)
btn_create_client.place(x=240, y=300)
### end client ###
### product ######
label_product_name = tk.Label(text="Name:")
label_product_price = tk.Label(text="DNI:")
entry_product_name = tk.Entry()
entry_product_price = tk.Entry()
btn_create_product = tk.Button(text="Crear Product", command=add_product, width=20)
label_product_name.place(x=10, y=450)
label_product_price.place(x=10, y=550)
entry_product_name.place(x=200, y=550)
entry_product_price.place(x=200, y=550)
btn_create_product.place(x=240, y=600)
### end product ##

### sales ########
combo_clients = Combobox(
    values = ['hola']
)
combo_products = Combobox(
    values = ['chau']
)

entity_sale_qty = tk.Entry()

combo_clients.place(x=10, y=100)
btn_create_sale = tk.Button(text="Crear Venta", command=add_sale, width=20)
btn_create_sale.place(x=240, y=900)
### end sale #####

window.config(width=700, height=1000)
window.mainloop()