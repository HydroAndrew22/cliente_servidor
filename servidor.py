import socket
import psycopg2

# Configuración de la base de datos PostgreSQL
DB_HOST = "localhost"    # modificar
DB_PORT = 5432
DB_NAME = "bd"           # modificar
DB_USER = "user"         # modificar
DB_PASSWORD = "password" # modificar

# Función para consultar la base de datos y obtener información del número de teléfono
def consultar_telefono(numero_telefono):
    try: # configuración del entorno
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER,
            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = conn.cursor() # Consulta a ejecutar
        cursor.execute("""SELECT p.dir_tel as "Telefono", p.dir_nombre as "Nombre",
                        p.dir_direccion as "Dirección",
                        c.ciud_nombre as "Ciudad"
                        from sist_distri.personas p 
                        left join sist_distri.ciudades c on p.dir_ciud_id = c.ciud_id
                        where p.dir_tel = %s""", (numero_telefono,))

        row = cursor.fetchone() # Recupera de los resultados de la consulta
        cursor.close() # cierre de conexion a la BD
        conn.close()
        return row
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Función para iniciar el servidor
def iniciar_servidor():
    # Creación del objeto, con socket tipo TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Permite reutilizar la dirección
    servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    servidor_socket.bind(('localhost', 9999)) # Vinculación del socket
    servidor_socket.listen(5) # # max de conexiones
    print("Servidor esperando conexiones...")

    while True:
        conexion, direccion = servidor_socket.accept()
        print("Conexión establecida . . .")

        # Recibe el número de teléfono del cliente
        numero_telefono = conexion.recv(1024).decode()

        # Verifica si la entrada es un número
        if not numero_telefono.isdigit():
            resultado = "Error: El número de teléfono ingresado no es válido."
            conexion.send(resultado.encode())
        else:
            # Consulta la base de datos
            resultado = consultar_telefono(numero_telefono)

            # Envia el resultado al cliente
            if resultado:
                mensaje = f"Número de Teléfóno: {resultado[0]}\nNombre:             {resultado[1]} \nDirección:          {resultado[2]} \nCiudad:             {resultado[3]}"
            else:
                mensaje = "Persona dueña de ese número telefónico no existe."
            conexion.send(mensaje.encode())

        conexion.close()

if __name__ == "__main__":
    iniciar_servidor()


