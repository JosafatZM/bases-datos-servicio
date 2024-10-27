import os 
import pandas as pd

"""
Este script realiza la transformación de datos almacenados en archivos .xlsx a archivos .csv. 
Este proceso facilita la manipulación y análisis de los datos, permitiendo un acceso más eficiente y una 
interacción más sencilla con herramientas de procesamiento de datos. 
Los archivos .csv generados pueden ser utilizados en diversos entornos de análisis y visualización, 
mejorando la flexibilidad en la gestión de datos.
"""


# inserta el path de la carpeta donde se encuentren los archivos '.xlsx'
carpeta =r"C:\Users\user\ruta"

for root, dirs, files in os.walk(carpeta):
    for file in files:
        df = pd.read_excel(f"{carpeta}\{file}")
        print(f"leyendo: {file}")
        # se hace este paso porque la nomenclatura de los archivos que tenia era 'genero_sujeto_#sujeto'
        splity_file_name = file.split('_')
        # nombre del archivo CSV de salida
        output_path = f"datos_{splity_file_name[0]}_{splity_file_name[2]}.csv"

        df.to_csv(output_path, index=False)

        print(f"Archivo {file} convertido exitosamente a {output_path}")

        