ETL (Extract, Transform, Load) es el proceso de extracción, transformación y carga de datos, 
esencial en proyectos de datos para garantizar datos consistentes y listos para el análisis y modelado.

- Extract (Extracción): Se obtienen datos desde diversas fuentes, como bases de datos o archivos. 
Esto permite consolidar datos relevantes en un solo lugar.
- Transform (Transformación): Los datos se limpian y transforman mediante operaciones como normalización, 
eliminación de valores atípicos y generación de nuevas variables. Esta etapa prepara los datos en el formato 
ideal para su analisis.
- Load (Carga): Los datos transformados se cargan en un sistema de almacenamiento o base de datos que el 
equipo puede utilizar.


ETL en "structure_data2csv", facilita la extracción y preparación de datos de señales EEG 
para su análisis posterior. 

- Extracción: El código obtiene datos de múltiples canales de una estructura preprocesada. 
- Transformación: Se asegura de que cada matriz de señal tenga un tamaño uniforme de 16 filas, 
rellenando con NaN cuando es necesario, lo que es crucial para mantener la consistencia en el análisis. 
- Carga: Los datos transformados se guardan en archivos CSV, lo que permite su fácil acceso y utilización en 
futuros análisis

ETL en "upload_EEGs2DataBase" la justificación del proceso ETL en este código es fundamental para asegurar 
la calidad y utilidad de los datos de EEG. 

- Extracción: Los datos se extraen de múltiples archivos CSV, lo que permite reunir información de diferentes
registros en un solo proceso.
- Transformación: Aunque el código no realiza transformaciones complejas, convierte los datos en listas de lista
y luego a formato JSON. Esta transformación es crucial para garantizar que los datos estén en un formato adecuado 
para ser almacenados en la base de datos, facilitando su posterior análisis y consulta.
- Carga: Finalmente, los datos transformados se cargan en una tabla de MySQL. Este paso permite la integración de 
los datos en un sistema de gestión que facilita el acceso y análisis futuros
