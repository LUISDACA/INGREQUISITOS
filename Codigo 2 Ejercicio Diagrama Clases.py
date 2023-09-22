class Cliente:
    def __init__(self, codigo, dni, nombre, direccion, telefono, aval=None):
        self.codigo = codigo
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.aval = aval

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Reserva:
    def __init__(self, cliente, coche, fecha_inicio, fecha_final, precio_alquiler, entregado=False, agencia=None):
        self.cliente = cliente
        self.coche = coche
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.precio_alquiler = precio_alquiler
        self.entregado = entregado
        self.agencia = agencia

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre


cliente1 = Cliente(1, "123456789", "Cliente 1", "Dirección 1", "123-456-789")
cliente2 = Cliente(2, "987654321", "Cliente 2", "Dirección 2", "987-654-321")
cliente3 = Cliente(3, "111111111", "Cliente 3", "Dirección 3", "111-111-111", cliente1)


coche1 = Coche("ABC123", "Camaro", "Rojo", "Chevrolet", "Garaje 1")
coche2 = Coche("DEF456", "Hilux", "Azul", "Toyota", "Garaje 2")


def mostrar_coches_disponibles(coches):
    print("Coches disponibles:")
    for i, coche in enumerate(coches, 1):
        print(f"{i}. Matrícula: {coche.matricula}, Modelo: {coche.modelo}, Marca: {coche.marca}")

12312
print("Bienvenido a la empresa de alquiler de automóviles.")
dni = input("Ingrese su Cedula: ")
nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su teléfono de contacto: ")


mostrar_coches_disponibles([coche1, coche2])
opcion = int(input("Seleccione el número del coche que desea alquilar: "))

if opcion == 1:
    coche_seleccionado = coche1
elif opcion == 2:
    coche_seleccionado = coche2
else:
    print("Opción no válida. Seleccionando el coche 1 por defecto.")
    coche_seleccionado = coche1

fecha_inicio = input("Ingrese la fecha de inicio de la reserva (YYYY-MM-DD): ")
fecha_final = input("Ingrese la fecha final de la reserva (YYYY-MM-DD): ")
precio_alquiler = float(input("Ingrese el precio de alquiler: "))


reserva = Reserva(Cliente(0, dni, nombre, direccion, telefono), coche_seleccionado, fecha_inicio, fecha_final, precio_alquiler)
reservas = [reserva]


print("\nReserva generada:")
print("Cliente:", reserva.cliente.nombre)
print("Coche:")
print(f"  Matrícula: {reserva.coche.matricula}, Modelo: {reserva.coche.modelo}, Marca: {reserva.coche.marca}")
print("Fecha de inicio:", reserva.fecha_inicio)
print("Fecha final:", reserva.fecha_final)
print("Precio de alquiler:", reserva.precio_alquiler)