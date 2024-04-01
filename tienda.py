class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__productos = []
        self.__costo_delivery = costo_delivery

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p.get_nombre() == producto.get_nombre():
                p.set_stock(p.get_stock() + producto.get_stock())
                return
        self.__productos.append(producto)

    def listar_productos(self):
        lista = ""
        for producto in self.__productos:
            nombre = producto.get_nombre()
            precio = producto.get_precio()
            stock = producto.get_stock()
            if isinstance(self, Supermercado):
                if stock < 10:
                    lista += f"{nombre}: Pocos productos disponibles ({stock})\n"
                else:
                    lista += f"{nombre}: {stock}\n"
            elif isinstance(self, Farmacia):
                if precio > 15000:
                    lista += f"{nombre}: Envío gratis al solicitar este producto ({precio})\n"
                else:
                    lista += f"{nombre}: {precio}\n"
            else:  # Restaurante
                lista += f"{nombre}: Stock 0 (fabricado al momento de venta)\n"
        return lista

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.get_nombre() == nombre_producto:
                if isinstance(self, Restaurante):
                    return  # No se hace nada en el caso del restaurante
                elif isinstance(self, Farmacia) and cantidad > 3:
                    return  # No se puede solicitar más de 3 productos en farmacia
                elif producto.get_stock() >= cantidad:
                    producto.set_stock(producto.get_stock() - cantidad)
                    return
                else:
                    producto.set_stock(0)
                    return


class Restaurante(Tienda):
    pass


class Supermercado(Tienda):
    pass


class Farmacia(Tienda):
    pass
