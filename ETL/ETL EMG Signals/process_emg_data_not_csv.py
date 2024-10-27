import os 
import csv

"""
Este código realiza un proceso de Extracción, Transformación y Carga (ETL)** para convertir archivos de texto de datos de electromiografía (EMG) en archivos CSV. 

Resumen del Proceso ETL:

1. Extracción: Recorre una carpeta y subcarpetas, abriendo archivos de texto que contienen datos EMG.
2. Transformación: Procesa los datos para eliminar líneas vacías y separa los valores relevantes, convirtiéndolos a tipo `float`.
3. Carga: Escribe los valores transformados en nuevos archivos CSV, generando nombres de archivo basados en el sujeto, lo que facilita la organización y análisis posterior de los datos.

Este flujo de trabajo permite una gestión eficiente y organizada de los datos EMG, facilitando su posterior análisis y visualización.
"""


carpeta = r'C:\route_to\EMG_not_csv'

# itera sobre todos los archivos y subcarpetas en la carpeta especificada 
for root, dirs, files in os.walk(carpeta):
    for file in files:
        emg_values = []
        # construye la ruta completa del archivo 
        path_copleto = os.path.join(root, file)

        # abrir archivo y leer su contenido 
        with open(path_copleto, "r") as emg_file:
            print(f"The file has been opened! {file}")
            content = emg_file.read()
            content_values = content.split('\n')
            content_values = content_values[:-1]
            for chunk in content_values:
                splity= chunk.split(' ')
                splity = splity[1:-1]
                for value in splity:
                    emg_values.append(float(value))

        name_splity = file.split('_')
        
        archivo_csv = f'M_sujeto_{name_splity[2]}.csv'
        print(emg_values[0:10])
        # Escribir en el archivo CSV
        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escribir cada dato en una nueva fila (columna única)
            for dato in emg_values:
                writer.writerow([dato])

        print(f"Archivo {archivo_csv} generado con éxito.")
    
        print(f"The file {file} has been closed!!")


print("se han leido todos los archivos de la carpeta con exito!")

"""
Orden de apertura de los archivos 

M_Sujeto_10_1.txt
M_Sujeto_11_1.txt
M_Sujeto_7_1.txt
M_Sujeto_8_1.txt

"""