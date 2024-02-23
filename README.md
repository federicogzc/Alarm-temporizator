<h2>Temporizador con Alarma</h2>
<p>Este script de Python crea un temporizador que cuenta hacia atrás por una duración especificada por el usuario en segundos. Al finalizar el conteo, se reproduce un archivo de sonido. Es útil para recordatorios o como una herramienta de gestión del tiempo.</p>

<h3>Funcionalidades</h3>
<ul>
  <li><strong>Conteo Regresivo</strong>: Permite al usuario establecer un temporizador especificando la duración en segundos.</li>
  <li><strong>Reproducción de Sonido</strong>: Al finalizar el conteo, reproduce automáticamente un archivo de sonido.</li>
</ul>

<h3>Cómo Funciona</h3>
<ol>
  <li>
    <strong>Inicio del Programa</strong>:
    <p>El programa comienza solicitando al usuario que introduzca la duración del temporizador en segundos. Si el valor ingresado no es un número entero, se muestra un mensaje de error y el programa termina.</p>
  </li>
  <li>
    <strong>Funcionamiento del Temporizador</strong>:
    <p>Utiliza la función <code>start_timer</code> para iniciar el conteo regresivo. Esta función imprime un mensaje indicando la duración del temporizador y luego pausa la ejecución del programa usando <code>time.sleep(duration)</code> por la cantidad de segundos especificada. Una vez completado el conteo, imprime un mensaje de finalización y llama a la función <code>play_sound</code>.</p>
  </li>
  <li>
    <strong>Reproducción del Sonido</strong>:
    <p>La función <code>play_sound</code> se encarga de abrir y reproducir un archivo de sonido. Es importante actualizar la variable <code>filepath</code> con la ruta correcta al archivo que se desea reproducir. Para la reproducción del sonido, el script utiliza el comando <code>os.system</code> con <code>xdg-open</code> en sistemas Linux, lo que permite abrir el archivo con su programa predeterminado.</p>
  </li>
</ol>

<h3>Consideraciones</h3>
<ul>
  <li><strong>Compatibilidad</strong>: El comando para reproducir el sonido está configurado para sistemas basados en Linux. Para otros sistemas operativos, será necesario modificar el comando según corresponda.</li>
  <li><strong>Ruta del Archivo de Sonido</strong>: Asegúrese de actualizar la ruta al archivo de sonido en la función <code>play_sound</code> para reflejar la ubicación correcta del archivo que desea reproducir.</li>
</ul>

<h3>Ejemplo de Uso</h3>
<pre>
<code>Introduce la duración del temporizador en segundos: 10
Temporizador iniciado para 10 segundos.
# Espera 10 segundos
¡Tiempo terminado!
# Reproduce el archivo de sonido</code>
</pre>

<p>Este script es ideal para quienes buscan una solución simple para gestionar el tiempo o necesitan un recordatorio audible después de un intervalo específico.</p>
