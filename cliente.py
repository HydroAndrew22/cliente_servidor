import socket

#Función para interactuar con el servidor
def interactuar_servidor():
    
    while True:  # Ciclo para permitir a usuario consultar varios números

        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creación del objeto, con socket tipo TCP
        cliente_socket.connect(('localhost', 9999)) # Conexión al servidor en el puerto descrito 192.168.10.114
        numero_telefono = input("Ingrese el número de teléfono: ") # Ingreso numero
        cliente_socket.send(numero_telefono.encode()) # envío del # telefónico ingresado al servidor
        respuesta = cliente_socket.recv(1024).decode() # Respuesta del servidor y casteo a cadena de texto
        print("+ - - - - - - - - Respuesta del servidor- - - - - - - - +\n")
        print(respuesta, "\n")
        print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - +\n")
        cliente_socket.close() # Como socket es TCP, se debe cerrar la conexión para solicitar otra petición

        # Si usuario escribe no/NO, finaliza la ejecución
        respuesta = input("¿Deseas ingresar otro número? (escribe NO para salir): ")
        if respuesta.upper() == "NO":
            print("\n+ - - - - - - - -  Hasta Pronto  - - - - - - - - +")
            print("+ - - - - - - - - - - - - - - - -  - - - - - - - - +\n")
            break

# Inicialización del script
if __name__ == "__main__":
    interactuar_servidor()
