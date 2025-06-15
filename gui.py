import PySimpleGUI as sg
from timer import start_timer
from stats import get_total_today

def run_gui():
    layout = [
        [sg.Text('Pomodoro App', font=('Helvetica', 20), justification='center')],
        [sg.Text('25:00', key='-TIMER-', font=('Helvetica', 48), justification='center')],
        [sg.Button('Iniciar'), sg.Button('Detener', visible=False), sg.Button('Salir')],
        [sg.Text('', key='-STATS-', font=('Helvetica', 12))]
    ]

    window = sg.Window('Pomodoro Timer', layout, element_justification='center')

    while True:
        event, _ = window.read(timeout=100)

        if event in (sg.WIN_CLOSED, 'Salir'):
            break
        elif event == 'Iniciar':
            window['Detener'].update(visible=True)
            start_timer(25 * 60, window)
            window['Detener'].update(visible=False)

        window['-STATS-'].update(f"Pomodoros completados hoy: {get_total_today()}")

    window.close()
