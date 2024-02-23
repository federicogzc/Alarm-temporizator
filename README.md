# Temporizador con Alarma 🕒🔊

Este script de Python permite a los usuarios establecer un temporizador en segundos, minutos u horas. Una vez completado el tiempo, el script reproduce automáticamente un archivo de sonido para notificar al usuario.

## 🚀 Funcionamiento

1. El usuario ejecuta el script.
2. Se solicita al usuario que introduzca la unidad de tiempo (`segundos`, `minutos`, `horas`) y la duración del temporizador.
3. El script cuenta hacia atrás hasta que el tiempo se agota.
4. Al finalizar, se reproduce un archivo de sonido especificado en el código.

## 📌 Requisitos

- Python 3.x
- Acceso a la terminal o línea de comandos.
- Un archivo de audio o video en formato MP4 para la alarma (ajustar la ruta en el script).

## 🛠️ Instalación y Uso
git clone <url-del-repositorio>
cd <directorio-del-repositorio>
python temporizador.py
Sigue las instrucciones en pantalla para configurar el temporizador.

## ⚙ Configuración
Para personalizar el sonido de la alarma, actualiza la variable filepath en la función 'play_sound()' con la ruta a tu archivo de audio o video.

filepath = "/ruta/a/tu/archivo.mp4"

## 🤔 Solución de Problemas
Asegúrate de que el archivo MP4 exista en la ruta especificada.
Este script ha sido probado en entornos Linux. Para otros sistemas operativos, puede ser necesario modificar el comando para abrir el archivo de sonido.
📝 Licencia
Este proyecto está bajo la Licencia MIT.

¡Esperamos que este temporizador te ayude a gestionar tu tiempo de manera eficiente! 🚀✨


