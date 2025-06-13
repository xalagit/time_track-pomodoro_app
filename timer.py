from datetime import datetime
from database import log_session

def start_timer(duration, window):
    start_time = datetime.now()

    while duration > 0:
        mins, secs = divmod(duration, 60)
        window['-TIMER-'].update(f'{mins:02}:{secs:02}')
        event, _ = window.read(timeout=1000)
        if event in (None, 'Salir'):
            return  # Detener si el usuario cierra la ventana o presiona salir
        duration -= 1

    window['-TIMER-'].update("¡Tiempo!")
    end_time = datetime.now()
    total_secs = int((end_time - start_time).total_seconds())
    log_session(start_time, end_time, total_secs)
