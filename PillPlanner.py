import PySimpleGUI as sg

sg.theme = 'monoblue'  # please make your windows colorful

layout = [[sg.Button('Input Medication')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show', size=(50,5)), sg.Button('Exit')]]

window = sg.Window('TAKE YOUR FUCKING PILLZ!!', 
                   layout, 
                   size = (1000, 750),
                   resizable = True)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close(

#hello there