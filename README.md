<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Descripción del Código</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .icon {
            padding-right: 8px;
            color: #007bff;
        }
    </style>
</head>
<body>
    <h1>Descripción del Código</h1>
    <p><i class="fas fa-code icon"></i>Este script en Python es un temporizador personalizable que puede ser configurado para contar segundos, minutos u horas. Al finalizar el conteo, reproduce un sonido.</p>
    
    <h2>Funcionamiento</h2>
    <ol>
        <li><i class="fas fa-user-clock icon"></i>El usuario introduce la unidad de tiempo (<code>segundos</code>, <code>minutos</code>, <code>horas</code>) y la duración.</li>
        <li><i class="fas fa-hourglass-start icon"></i>El script convierte la duración a segundos (si es necesario) y comienza el temporizador.</li>
        <li><i class="fas fa-sleep icon"></i>El programa espera (en pausa) por la duración especificada.</li>
        <li><i class="fas fa-bell icon"></i>Cuando el tiempo se agota, se muestra un mensaje y se reproduce un sonido.</li>
    </ol>
    
    <h2>Detalles Técnicos</h2>
    <ul>
        <li><i class="fas fa-clock icon"></i>Usa <code>time.sleep()</code> para esperar el tiempo especificado.</li>
        <li><i class="fas fa-play-circle icon"></i>Reproduce un sonido abriendo un archivo MP4 con el programa predeterminado del sistema para este tipo de archivo.</li>
        <li><i class="fas fa-exclamation-triangle icon"></i>Requiere que la ruta al archivo de sonido esté correctamente configurada en la función <code>play_sound()</code>.</li>
        <li><i class="fas fa-cogs icon"></i>La compatibilidad para abrir archivos es específica de Linux usando <code>xdg-open</code>.</li>
    </ul>
    
    <h2>Consideraciones</h2>
    <p><i class="fas fa-info-circle icon"></i>Es importante asegurarse de que la ruta al archivo MP4 sea accesible y correcta para evitar errores al intentar reproducir el sonido.</p>
</body>
</html>
