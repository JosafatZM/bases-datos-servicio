import mysql.connector

"""
Este código transforma los datos al simplificar la identificación de los sujetos. 
Los nombres originales, como 'ADT_P05_S1', eran complejos y difíciles de interpretar. 
La transformación permite extraer información valiosa, como la terapia, el número de 
paciente y el número de sesión. Este enfoque no solo mejora la estructura de los datos,
sino que también facilita el filtrado y la consulta en el futuro, lo que resulta en una 
gestión de datos más eficiente y efectiva.
"""



# Establece los detalles de la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="registros_pres"
)

# Comprueba si la conexión se ha establecido correctamente
if conexion.is_connected():
    print("Conexión exitosa")

# lo que nos permite interacturar con las beses de datos
cursor = conexion.cursor()

# Cadena de texto con los nombres de los sujetos en formato Matlab
matlab_syntaxis = (
    r"ADT_P05_S1'ADT_P05_S4'ADT_P10_S1'ADT_P10_S4'Binaural_P03_S1'Binaural_P03_S4'"
    r"Binaural_P16_S1'Binaural_P16_S4'Control_P01_S1'Control_P01_S4'Control_P02_S1'"
    r"Control_P02_S4'Control_P03_S1'Control_P03_S4'Control_P04_S1'Control_P04_S4'"
    r"Control_P05_S1'Control_P05_S4'Control_P07_S1'Control_P07_S4'Control_P08_S1'"
    r"Control_P08_S4'Control_P11_S1'Control_P11_S4'Control_P09_S1'Control_P12_S1'"
    r"Control_P14_S1'EAE_P08_S1'EAE_P08_S4'EAE_P10_S1'EAE_P10_S4'Placebo_P05_S1'"
    r"Placebo_P05_S4'Placebo_P09_S1'Placebo_P09_S4'TRT_P03_S1'TRT_P03_S4'TRT_P08_S1'"
    r"TRT_P08_S4'TRT_P12_S1'TRT_P12_S4"
)
# Separar el string en una lista de sujetos
sujetos = matlab_syntaxis.split(r"'")

# Listas para almacenar la información separada
terapia = []
no_pasiente = []
no_sesion = []

# Iterar sobre cada registro en la lista de sujetos
for registro in sujetos:
    # Separar el registro utilizando el guion bajo como delimitador
    registro_split = registro.split("_")
    terapia.append(registro_split[0])
    # Extraer y almacenar el número de paciente y sesion, eliminando los caracteres no numéricos
    no_pasiente.append(int(registro_split[1][-2:]))
    no_sesion.append(int(registro_split[2][-1]))

# for i in range(0, 41):
#     print(terapia[i], no_pasiente[i], no_sesion[i])


for i in range(len(terapia)):
    # Extraer los valores de terapia, paciente y sesión
    sql_terapia = terapia[i]
    sql_pasiente = int(no_pasiente[i])
    sql_sesion = int(no_sesion[i])
      
    query = "INSERT INTO registros_pres.sujetos (Terapia, Paciente, Sesion) VALUES (%s, %s, %s)" # -> placeholders
    
    # Ejecutar la consulta SQL con los valores correspondientes
    cursor.execute(query, (sql_terapia, sql_pasiente, sql_sesion))
    
    # Actualizar la tabla
    conexion.commit()



# close connection with data base
cursor.close()
conexion.close()

print("Datos guardados correctamente!")