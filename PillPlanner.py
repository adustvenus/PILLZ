import HEAD as HEAD
import PySimpleGUI as sg
sg.theme= 'monoblue' # please make your windows colorful


<<<<<<< HEAD
layout = [
        [sg.Button('Input Medication')],
          [sg.Input(key='-med-')],
          [sg.Button('Show', size=(20,1)),
    ],
        [sg.Button('Cost')],
        [sg.Input(key='-cost-')],
        [sg.Button('show', size=(20,1))
     ],
        [sg.Button('weekly amount')],
        [sg.Input(key='-week-')],
        [sg.Button('show', size=(20,1))],
    [
        [sg.Button("Day of the Week")],
        [sg.Input(key="-day-")],
        [sg.Button('show', size=(20,1))]
    ]
]

=======
a = [sg.Text('~ Pill Planner ~ ',
             justification='center',
             size=(100,1))]


layout = [a,
          [sg.Input(key='-IN-')],
          [sg.Button('Show', size=(50,5)), sg.Button('Exit')]]

window = sg.Window('TAKE YOUR FUCKING PILLZ!!', 
                   layout,
                   size = (1000, 750),
                   resizable = True)
>>>>>>> origin/main

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

<<<<<<< HEAD

window.close()


=======
window.close()
>>>>>>> origin/main
