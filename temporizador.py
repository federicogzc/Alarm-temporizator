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
    unidad = input("Introduce la unidad de tiempo (segundos, minutos, horas): ").lower()
    duracion = input("Introduce la duración del temporizador: ")

    try:
        duracion = int(duracion)
        if unidad == "minutos":
            duracion *= 60  # Convertir minutos a segundos
        elif unidad == "horas":
            duracion *= 3600  # Convertir horas a segundos
        elif unidad != "segundos":
            raise ValueError("Unidad de tiempo no reconocida.")

        start_timer(duracion)
    except ValueError as e:
        if str(e) == "Unidad de tiempo no reconocida.":
            print(e)
        else:
            print("Por favor, introduce un número entero como duración.")
