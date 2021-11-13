import PySimpleGUI as sg
import random
import string
sg.theme= 'monoblue' # please make your windows colorful

#
#Initialize variables for pages
#

font = ("Impact", 31)

title = [sg.Text('~ Pill Planner ~ ',
             size=(100,None),
             expand_x = True,
             justification='center',
             font = font,
             text_color = None)
         ]

#
#Functions for buttons
#
def pill_adder_button():
    layout = [
        [sg.Button('Input Medication')],
          [sg.Input(key='-med-')],
          [sg.Button('Show', size=(20,1)),
    ],
    [
        [sg.Button('Cost')],
        [sg.Input(key='-cost-')],
        [sg.Button('show', size=(20,1))],
    ],
    [
        [sg.Button('weekly amount')],
        [sg.Input(key='-week-')],
        [sg.Button('show', size=(20,1))],
    ],
    [
        [sg.Button("Day of the Week")],
        [sg.Input(key="-day-")],
        [sg.Button('show', size=(20,1))]
    ]
]

    window = sg.Window("Medication Adder", 
                       layout,
                       size = (1000, 750),
                       resizable = True,
                       modal = True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()
#
#Title Page
#
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=10, num_cols=7)
headings = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


#headings = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

daysofweek = [sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    background_color='dark blue',
                    auto_size_columns=True,
                    justification='center',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=25)
    ]

layout = [
            daysofweek,
            title,
            [sg.Button('Add Pill'), ],
            [sg.Button('Show', size=(20,5)),  sg.Button('Exit')]
         ]


window = sg.Window('TAKE YOUR FUCKING PILLZ!!', 
                   layout,
                   size = (1500, 1000),
                   resizable = False)



while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Pill':
        # change the "output" element to be the value of "input" element
        pill_adder_button()

window.close()