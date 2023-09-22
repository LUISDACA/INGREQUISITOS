class Empleado:
    def __init__(self, nombre, edad, sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Cliente:
    def __init__(self, nombre, edad, telefono_contacto):
        self.nombre = nombre
        self.edad = edad
        self.telefono_contacto = telefono_contacto

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_empleados(self):
        print("Empleados de la empresa", self.nombre)
        for empleado in self.empleados:
            if isinstance(empleado, Directivo):
                print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Sueldo Bruto: {empleado.sueldo_bruto}, Categoría: {empleado.categoria}")
                print("Subordinados:")
                for subordinado in empleado.subordinados:
                    print(f"   - {subordinado.nombre}")
            else:
                print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Sueldo Bruto: {empleado.sueldo_bruto}")

    def mostrar_clientes(self):
        print("Clientes de la empresa", self.nombre)
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre}, Edad: {cliente.edad}, Teléfono de Contacto: {cliente.telefono_contacto}")


# Solicitar datos al usuario
nombre_empresa = input("Nombre de la empresa: ")
mi_empresa = Empresa(nombre_empresa)

while True:
    tipo_registro = input("\n¿Qué desea agregar (empleado/cliente)? (Ingrese 'salir' para finalizar): ").lower()

    if tipo_registro == 'salir':
        break
    elif tipo_registro == 'empleado':
        nombre = input("Nombre del empleado: ")
        edad = int(input("Edad del empleado: "))
        sueldo_bruto = float(input("Sueldo bruto del empleado: "))
        categoria = input("Categoría (si es directivo, de lo contrario, presione Enter): ")
        if categoria:
            empleado = Directivo(nombre, edad, sueldo_bruto, categoria)
            subordinados = input("¿Tiene subordinados? (si/no): ").lower()
            if subordinados == 'si':
                while True:
                    nombre_subordinado = input("Nombre del subordinado (o 'fin' para terminar): ")
                    if nombre_subordinado.lower() == 'fin':
                        break
                    edad_subordinado = int(input("Edad del subordinado: "))
                    sueldo_bruto_subordinado = float(input("Sueldo bruto del subordinado: "))
                    subordinado = Empleado(nombre_subordinado, edad_subordinado, sueldo_bruto_subordinado)
                    empleado.agregar_subordinado(subordinado)
        else:
            empleado = Empleado(nombre, edad, sueldo_bruto)

        mi_empresa.agregar_empleado(empleado)
    elif tipo_registro == 'cliente':
        nombre = input("Nombre del cliente: ")
        edad = int(input("Edad del cliente: "))
        telefono_contacto = input("Teléfono de contacto del cliente: ")
        cliente = Cliente(nombre, edad, telefono_contacto)
        mi_empresa.agregar_cliente(cliente)

mi_empresa.mostrar_empleados()
mi_empresa.mostrar_clientes()