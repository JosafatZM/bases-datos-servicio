
import os 
import csv

"""
Este script recorre una carpeta y sus subcarpetas para procesar archivos de texto que contienen datos de EMG (electromiografía). 
Para cada archivo encontrado, el script realiza las siguientes acciones:

1. Lectura: Abre el archivo y lee su contenido, separando los valores por comas.
2. Transformación: Convierte los valores leídos a tipo float y los almacena en una lista. El nombre del archivo CSV de salida se genera en función del prefijo del archivo original, 
indicando si el sujeto es femenino ('F') o masculino ('M').
3. Carga: Escribe los datos transformados en un nuevo archivo CSV con un nombre correspondiente al sujeto, creando así una estructura organizada de los datos.

Finalmente, el script imprime mensajes de progreso durante la ejecución, informando sobre la apertura y cierre de archivos, así como la generación exitosa de los archivos CSV.
"""



carpeta = r'C:\Users\user'

# itera sobre todos los archivos y subcarpetas en la carpeta especificada 
for root, dirs, files in os.walk(carpeta):
    for file in files:
        global emg_values
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
                splity= chunk.split(',')
                for value in splity:
                    emg_values.append(float(value))

        splity_file_name = file.split("_")
        if splity_file_name[0] == "F":
            global lista_name 
            lista_name = f'F_sujeto_{splity_file_name[2]}'  # Crear el nombre de la lista
            
        else:
            lista_name = f'M_sujeto_{splity_file_name[2]}'  # Crear el nombre de la lista
            

        archivo_csv = f'{lista_name}.csv'
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

F_Sujeto_10_1.txt
F_Sujeto_1_1.txt 
F_Sujeto_2_1.txt
F_Sujeto_3_1.txt
F_Sujeto_4_1.txt
F_Sujeto_5_1.txt
F_Sujeto_6_1.txt
F_Sujeto_7_1.txt
F_Sujeto_8_1.txt
F_Sujeto_9_1.txt
M_Sujeto_1_1.txt
M_Sujeto_2_1.txt
M_Sujeto_3_1.txt
M_Sujeto_4_1.txt
M_Sujeto_5_1.txt
M_Sujeto_6_1.txt
M_Sujeto_9_1.txt
"""





