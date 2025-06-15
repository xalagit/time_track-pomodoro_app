import PySimpleGUI as sg
from timer import start_timer
from stats import (
    get_total_today,
    get_total_week,
    get_total_month,
    get_hourly_distribution,
    format_h_mm
)

def show_stats_window():
    total_dia = get_total_today()
    total_semana = get_total_week()
    total_mes = get_total_month()
    horas = get_hourly_distribution(format_h_mm)

    layout = [
        [sg.Text('Estadísticas', font=('Helvetica', 16))],
        [sg.Text(f"Tiempo trabajado hoy: {format_h_mm(total_dia)}")],
        [sg.Text(f"Tiempo trabajado esta semana: {format_h_mm(total_semana)}")],
        [sg.Text(f"Tiempo trabajado este mes: {format_h_mm(total_mes)}")],
        [sg.Text("Horarios donde más trabajas:")],
        [sg.Multiline(horas, size=(40, 8), disabled=True)],
        [sg.Button('Cerrar')]
    ]
    window = sg.Window('Estadísticas', layout)
    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Cerrar'):
            break
    window.close()

def run_gui():
    layout = [
        [sg.Text('Pomodoro App', font=('Helvetica', 20), justification='center')],
        [sg.Text('25:00', key='-TIMER-', font=('Helvetica', 48), justification='center')],
        [sg.Button('Iniciar'), sg.Button('Detener', visible=False), sg.Button('Salir')],
        [sg.Button('Ver estadísticas', key='-STATS_BTN-')]
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
        elif event == '-STATS_BTN-':
            show_stats_window()

    window.close()
