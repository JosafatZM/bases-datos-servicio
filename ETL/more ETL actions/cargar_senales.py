import pandas as pd
import json

import mysql.connector

# Establece los detalles de la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DataBase98_!",
    database="registros_pres"
)

# lista con los canales utilizados en los EGG's de los PREs
canales = ['FP1', 'FP2', 'Fz', 'FC3','FCz', 'FC4', 'C5', 'C3', 'C1', 'Cz', 'C2', 'C4','C6', 'CP3', 'CPz', 'CP4']



# Comprueba si la conexión se ha establecido correctamente
if conexion.is_connected():
    print("Conexión exitosa")

# lo que nos permite interacturar con las beses de datos
cursor = conexion.cursor()



for registro in range(1, 42):
    ruta_general = r"C:\Users\Josaf\OneDrive - Universidad de Guadalajara\UdeG\7mo\Servicio\csv's pres"
    
    ruta_csv_05_30Hz = ruta_general + r"\05_30Hz\data_pres_{}.csv" 
    ruta_csv_delta = ruta_general + r"\Delta\data_pres_delta_{}.csv" 
    ruta_csv_theta = ruta_general + r"\Theta\data_pres_theta_{}.csv" 
    ruta_csv_alpha = ruta_general + r"\Alpha\data_pres_alpha_{}.csv" 
    ruta_csv_beta = ruta_general + r"\Beta\data_pres_beta_{}.csv" 
    ruta_csv_gamma = ruta_general + r"\Gamma\data_pres_gamma_{}.csv" 


    # Generar la ruta completa con el numero de archivo correspondiente 
    ruta_completa_05_30Hz = ruta_csv_05_30Hz.format(registro)
    ruta_completa_delta = ruta_csv_delta.format(registro)
    ruta_completa_theta = ruta_csv_theta.format(registro)
    ruta_completa_alpha = ruta_csv_alpha.format(registro)
    ruta_completa_beta = ruta_csv_beta.format(registro)
    ruta_completa_gamma = ruta_csv_gamma.format(registro)

    # leer cada csv 
    data_05_30Hz = pd.read_csv(ruta_completa_05_30Hz, sep=',', header= None)
    data_delta = pd.read_csv(ruta_completa_delta, sep=',', header= None)
    data_theta = pd.read_csv(ruta_completa_theta, sep=',', header= None)
    data_alpha = pd.read_csv(ruta_completa_alpha, sep=',', header= None)
    data_beta = pd.read_csv(ruta_completa_beta, sep=',', header= None)
    data_gamma = pd.read_csv(ruta_completa_gamma, sep=',', header= None)

    # Convierte el DataFrame en una lista de listas
    lista_05_30Hz = data_05_30Hz.values.tolist()
    lista_delta = data_delta.values.tolist()
    lista_theta = data_theta.values.tolist()
    lista_alpha = data_alpha.values.tolist()
    lista_beta = data_beta.values.tolist()
    lista_gamma = data_gamma.values.tolist()

    # Convertir la lista a JSON
    json_05_30Hz = json.dumps(lista_05_30Hz)
    json_delta = json.dumps(lista_delta)
    json_theta = json.dumps(lista_theta)
    json_alpha = json.dumps(lista_alpha)
    json_beta = json.dumps(lista_beta)
    json_gamma = json.dumps(lista_gamma)
    json_channels = json.dumps(canales)

    query = "INSERT INTO registros_pres.señales (ID_pres, Channels, `05-30 Hz`, Delta, Theta, Alpha, Beta, Gamma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    # ID_pres, Channels, 05-30Hz, Delta, Theta, Alpha, Beta, Gamma
    cursor.execute(query, (registro, json_channels, json_05_30Hz, json_delta, json_theta, json_alpha, json_beta, json_gamma,))
    # to update the table
    conexion.commit()


# close connection with data base
cursor.close()
conexion.close()

print("Datos guardados correctamente!")
