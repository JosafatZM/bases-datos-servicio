% El código en cuestión itera a través de 41 canales de señales EEG almacenadas en una estructura
% llamada `PREs`. Para cada canal, se accede a la señal correspondiente en `signals_gamma1` utilizando 
% `eval` para construir dinámicamente la ubicación de la señal. Luego, se verifica si la señal tiene 
% menos de 16 filas; si es así, se rellenan las filas restantes con `NaN` para asegurarse de que la matriz 
% resultante tenga exactamente 16 filas. Finalmente, la matriz ajustada se guarda en un archivo CSV, cuyo 
% nombre incluye el número del canal correspondiente, permitiendo así la exportación de las señales EEG en 
% un formato fácilmente manejable.


for channel = 1:41
    % Define la ubicación de la señal en la estructura preprocessed_signals
    registro_eeg_location = sprintf('PREs(%d).signals_gamma1', channel);
    
    % Utiliza eval para obtener la señal de la estructura
    registro_eeg = eval(registro_eeg_location);
    
    =
    % Ajusta el tamaño de la matriz para tener 16 filas
    if size(registro_eeg, 1) < 16
        registro_eeg = [registro_eeg; nan(16 - size(registro_eeg, 1), size(registro_eeg, 2))];
    end

    % Escribe la matriz en un archivo CSV
    nombre_archivo = sprintf("data_pres_gamma_%d.csv", channel);
    writematrix(registro_eeg, nombre_archivo);
end

% Conversión de Contenido de CSV a Listas
% - Facilidad de Manipulación: Convertir el contenido de un archivo CSV a listas en Python permite una manipulación más sencilla de los datos 
%   antes de su carga. Las listas son estructuras de datos más manejables y versátiles que permiten operaciones como iteraciones, filtrados y 
%   transformaciones.
% - Optimización de la Carga: Al usar listas, se puede preparar la información de manera más eficiente para la inserción en la base de datos. 
%   Esto reduce el tiempo de carga, ya que se puede realizar operaciones en lotes en lugar de insertar registros uno por uno.
% - Facilitación del Retrieve: Al almacenar los datos como listas, es posible realizar consultas más eficientes en la base de datos. 
%   Los datos organizados en listas pueden ser fácilmente convertidos de nuevo a estructuras que se adapten a las necesidades de recuperación,
%   permitiendo una manipulación rápida y flexible de la información
