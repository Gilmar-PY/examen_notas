import threading
import time
import random

def worker_thread(thread_id):
    # Cada hilo imprime su ID.
    print(f"El hilo {thread_id} está corriendo.")

    # Genera un tiempo de espera aleatorio entre 1 y 5 segundos.
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)

    # Mensaje de finalización del hilo.
    print(f"El hilo {thread_id} ha finalizado después de {sleep_time} segundos.")

# Lista para mantener los hilos.
threads = []

# Crear y lanzar 5 hilos.
for i in range(5):
    # Creamos el hilo.
    thread = threading.Thread(target=worker_thread, args=(i,))

    # Añadimos el hilo a la lista de hilos.
    threads.append(thread)

    # Iniciar el hilo.
    thread.start()

# Esperar a que todos los hilos terminen.
for thread in threads:
    thread.join()

print("Todos los hilos han finalizado.")
