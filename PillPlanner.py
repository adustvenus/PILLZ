import PySimpleGUI as sg
import random
import string
sg.theme= 'monoblue' # please make your windows colorful

#
#Initialize variables for pages


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
    [sg.Text("Please enter the medication's Name, Day Taken, Amount taken, and Price per bottle/unit")],
    [sg.Text('Name', size =(15, 1)), sg.InputText()],
    [sg.Text('Day Taken', size =(15, 1)), sg.InputText()],
    [sg.Text('Amount Taken', size =(15, 1)), sg.InputText()],
    [sg.Text('Price per Bottle/Unit', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
    window = sg.Window("Medication Adder", 
                       layout,
                       size = (800, 500),
                       resizable = True,
                       modal = True)
    event, values = window.read()
    window.close()
    pillz = open("Pillz.txt","a+")
    pillz.write(values[0])
    pillz.write("\n")
    pillz.write(values[1])
    pillz.write("\n")
    pillz.write(values[2])
    pillz.write("\n")
    pillz.write(values[3])
    pillz.write("\n")

    pillz.close
    return 
#Title Page
#
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table1(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

def make_table2(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data


# ------ Make the Table Data ------
data = make_table1(num_rows=10, num_cols=7)
headings = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

Cost = make_table2(num_rows=2, num_cols= 2)
headings2 = ['Pill', 'Cost']

layout = [  
            title,
            [sg.Button('Add Pill'), ],
            [sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
              background_color='dark blue',
              auto_size_columns=True,
              justification='center',
              num_rows=10,
              key='-TABLE1-',
              row_height=25)],
            [sg.Table(values=data[1:][:], headings=headings2, max_col_width=50,
              background_color='dark blue',
              auto_size_columns=True,
              justification='center',
              num_rows=2,
              key='-TABLE2-',
              row_height=20)],
            [sg.Button('Show', size=(8,2))],
            [sg.Button('Exit')]
]


window = sg.Window('Pharm-Tracker', 
                   layout,
                   size = (1000, 750),
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
