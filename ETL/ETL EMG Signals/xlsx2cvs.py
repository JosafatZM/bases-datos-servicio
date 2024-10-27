import os 
import pandas as pd

# inserta el path de la carpeta donde se encuentren los archivos '.xlsx'
carpeta =r"C:\Users\Josaf\OneDrive - Universidad de Guadalajara\UdeG\7mo\Servicio\bd_protocolo_CUCS\VIDEOS_grados" # en mi caso era esta ruta 

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

        