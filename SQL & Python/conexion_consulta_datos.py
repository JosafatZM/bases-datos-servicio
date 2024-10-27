# aqui se explica un poco mas que es un query y como crean una tabla basica 

import mysql.connector
from mysql.connector import Error

"""
1. ¿Qué es una consulta (query)?

Una consulta o query es una solicitud para interactuar con la base de datos.
Nos permite crear tablas, insertar datos, consultar información, actualizar registros,
y eliminar datos, entre otras acciones.
"""
try:
    # 2. Conectar a la base de datos
    # Cambia los valores de 'host', 'user', 'password' y 'database'
    # por los de tu propia configuración de MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="password",
        database="nombre_base_datos"
    )

    if connection.is_connected():
        print("Conexión a MySQL exitosa")

        # 3. Crear un cursor
        # El cursor nos permite ejecutar consultas SQL en la base de datos
        cursor = connection.cursor()

       # 4. Crear una tabla 
       # con los campos ID, Terapia, Paciente y Sesion
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS patients (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Terapia VARCHAR(50) NOT NULL,
            Paciente VARCHAR(50) NOT NULL,
            Sesion INT NOT NULL
        )
        '''
        cursor.execute(create_table_query)
        print("Tabla creada con éxito.")

        # 5. Insertar datos en la tabla
        # Insertamos algunos registros en la Tabla 
        insert_data_query = '''
        INSERT INTO patients (Terapia, Paciente, Sesion) VALUES 
            ('ADT', 5, 1),
            ('ADT', 1, 4),
            ('ADT', 3, 1)
        '''
        cursor.execute(insert_data_query)
        connection.commit()  # Confirma los cambios
        print("Datos insertados en la tabla")

        # 6. Consultar los datos de la tabla
        # Realizamos una consulta SELECT para obtener todos los registros de la Tabla
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)

        # 7. Imprimir los resultados
        # Obtenemos los datos y los mostramos en pantalla.
        rows = cursor.fetchall()
        print("Datos en la tabla:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Error conectando a MySQL: {e}")

# 8. Cerrar la conexión
# Cerramos la conexión con la base de datos para liberar los recursos
if connection.is_connected():
    cursor.close()
    connection.close()

