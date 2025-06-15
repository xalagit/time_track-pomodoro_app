from datetime import datetime
from database import log_session
import PySimpleGUI as sg

def start_timer(duration, window):
    start_time = datetime.now()
    tiempo_trabajado = 0

    while duration > 0:
        mins, secs = divmod(duration, 60)
        window['-TIMER-'].update(f'{mins:02}:{secs:02}')
        event, _ = window.read(timeout=1000)
        if event in (None, 'Salir', 'Detener'):
            end_time = datetime.now()
            tiempo_trabajado = int((end_time - start_time).total_seconds())
            if tiempo_trabajado > 0:
                log_session(start_time, end_time, tiempo_trabajado)
            return
        duration -= 1

    window['-TIMER-'].update("¡Tiempo!")
    end_time = datetime.now()
    total_secs = int((end_time - start_time).total_seconds())

    # Preguntar si quiere seguir trabajando
    respuesta = sg.popup_yes_no("¿Quieres seguir trabajando? Se activará un cronómetro.")
    if respuesta == "Yes":
        extra_secs = start_chronometer(window)
        total_secs += extra_secs
        end_time = datetime.now()
    log_session(start_time, end_time, total_secs)

def start_chronometer(window):
    start_extra = datetime.now()
    elapsed = 0
    while True:
        mins, secs = divmod(elapsed, 60)
        window['-TIMER-'].update(f'Extra: {mins:02}:{secs:02}')
        event, _ = window.read(timeout=1000)
        if event in (None, 'Salir', 'Detener'):
            break
        elapsed += 1
    return elapsed
