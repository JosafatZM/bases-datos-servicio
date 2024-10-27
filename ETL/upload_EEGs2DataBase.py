# Importamos las bibliotecas necesarias
import pandas as pd
import json
import mysql.connector

# 1. Establecemos los detalles de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",      # Cambia 'localhost' si tu base de datos está en un servidor diferente
    user="root",          # Tu nombre de usuario de MySQL
    password="password",          # Tu contraseña de MySQL
    database="nombre_base_datos"  # Especifica el nombre de tu base de datos
)

# 2. Definimos los canales de EEG que estamos utilizando
canales = ['FP1', 'FP2', 'Fz', 'FC3', 
           'FCz', 'FC4', 'C5', 'C3', 
           'C1', 'Cz', 'C2', 'C4',
           'C6', 'CP3', 'CPz', 'CP4']

# 3. Comprobamos si la conexión se ha establecido correctamente
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

# 4. Creamos un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# 5. Iteramos sobre un rango de registros, de 3 a 41 (ajusta según tus necesidades)
for registro in range(3, 42):
    # Definimos la ruta del archivo CSV
    ruta_archivo = r"ruta_a_la_carpeta_con\csv's\data_EEGs{}.csv"
    
    # Formateamos la ruta completa del archivo
    ruta_completa = ruta_archivo.format(registro)
    
    # 6. Leemos el archivo CSV en un DataFrame de Pandas
    data = pd.read_csv(ruta_completa, sep=',', header=None)
    
    # 7. Convertimos el DataFrame a una lista de listas
    lista_de_listas = data.values.tolist()
    
    # 8. Convertimos la lista a formato JSON para su almacenamiento
    json_lista = json.dumps(lista_de_listas)

    # 9. Preparamos la consulta SQL para insertar datos en la tabla
    query = "INSERT INTO registros_limpios.registros (canales) VALUES (%s)"
    
    # 10. Ejecutamos la consulta con los datos convertidos a JSON
    cursor.execute(query, (json_lista,))
    
    # 11. Confirmamos la transacción
    conexion.commit()

# 12. Cerramos la conexión con la base de datos
cursor.close()
conexion.close()

# Mensaje final para indicar que los datos se han guardado correctamente
print("Datos guardados correctamente!")