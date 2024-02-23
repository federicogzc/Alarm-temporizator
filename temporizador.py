import time
import os

def start_timer(duration):
    print(f"Temporizador iniciado para {duration} segundos.")
    time.sleep(duration)
    print("¡Tiempo terminado!")
    play_sound()

def play_sound():
    # Asegúrate de actualizar la ruta al archivo MP4 correctamente
    filepath = "/mnt/c/Users/Frederick/Desktop/proyectos/Code/itsMylife.mp4"
    # En Linux, utiliza 'xdg-open' para abrir archivos con su programa predeterminado
    os.system(f'xdg-open "{filepath}"')

if __name__ == "__main__":
    duracion = input("Introduce la duración del temporizador en segundos: ")
    try:
        duracion = int(duracion)
        start_timer(duracion)
    except ValueError:
        print("Por favor, introduce un número entero como duración.")
