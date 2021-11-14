import PySimpleGUI as sg
sg.theme= 'monoblue' # please make your windows colorful

#
#Initialize variables for pages


font = ("Impact", 31)

title = [sg.Text('~ Pharm Tracker ~ ',
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
    [sg.Text('Price per Bottle ($)', size =(15, 1)), sg.InputText()],
    [sg.Text('Amount in Bottle', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
    window = sg.Window("Medication Adder", 
                       layout,
                       size = (800, 500),
                       resizable = True,
                       disable_close = True,
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
    pillz.write(values[4])
    pillz.write("\n")

    pillz.close()
    return 

# ------ Make the Table Data ------

headings = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

headings2 = ['Pill', 'Cost ($)']

# ------ Table Data ------
table1data = []
holder = []
price = []
amountofpills = []


pillzdata = open("Pillz.txt","r")
readdata = pillzdata.readlines()
rows = int(len(readdata)/5)

for i in readdata:
    holder.append([i][0])

    if len(holder) == 5:
        print(holder)
        table1data.append(holder)
        price.append(int(holder[3])/int(holder[4]))
        amountofpills.append(holder[3])
        holder = []


amountofpills = [s.replace("\n", "") for s in amountofpills]
weeklycost = 0
for i in amountofpills:
    if i == "":
        i=0
    i = int(i)
    weeklycost = i + weeklycost



data1 = [["You", "Need", "To", "Add", "Your", "Pills", "Above"]]
for i in range(rows):
    if table1data[i][1] == 'Sunday\n':
                data1.append([(table1data[i][0]+"$"+table1data[i][2]), " ", " ", " ", " ", " ", " "])
    if table1data[i][1] == 'Monday\n':
                data1.append([" ", (table1data[i][0]+"$"+table1data[i][2]), " ", " ", " ", " ", " "])
    if table1data[i][1] == 'Tuesday\n':
                data1.append([" ", " ", (table1data[i][0]+"$"+table1data[i][2]), " ", " ", " ", " "])
    if table1data[i][1] == 'Wednesday\n':
                data1.append([" ", " ", " ", (table1data[i][0]+"$"+table1data[i][2]), " ", " ", " "])
    if table1data[i][1] == 'Thursday\n':
                data1.append([" ", " ", " ", " ", (table1data[i][0]+"$"+table1data[i][2]), " ", " "])
    if table1data[i][1] == 'Friday\n':
                data1.append([" ", " ", " ", " ", " ",(table1data[i][0]+"$"+table1data[i][2]), " "])
    if table1data[i][1] == 'Saturday\n':
                data1.append([" ", " ", " ", " ", " ", " ", (table1data[i][0]+"$" + table1data[i][2])])  
    if data1 != [["You", "Need", "To", "Add", "Your", "Pills", "Above"]] and data1[0] == ["You", "Need", "To", "Add", "Your", "Pills", "Above"]:
                data1.remove(["You", "Need", "To", "Add", "Your", "Pills", "Above"])
print(data1)

data2 = [["Input", "Pills"]]
for i in range(rows):
    if data1 !=[["You", "Need", "To", "Add", "Your", "Pills", "Above"]] and data2[0] ==["Input", "Pills"]:
        data2.remove(["Input", "Pills"])
    if data2 != ["Input", "Pills"]:
        data2.append([table1data[i][0], table1data[i][3]])

layout = [  
            title,
            [sg.Button('Add Pill'), sg.Button('Refresh')],
            
            [sg.Table(values=data1, headings=headings, max_col_width=25,
              background_color='dark blue',
              auto_size_columns=False,
              
              justification='center',
              num_rows=rows,
              hide_vertical_scroll = True,
              key='-TABLE1-',
              row_height=45)],
            
            [sg.Table(values=data2, headings=headings2, max_col_width=50,
              background_color='dark blue',
              auto_size_columns=True,
              justification='center',
              num_rows=rows,
              hide_vertical_scroll = True,
              key='-TABLE2-',
              row_height=20)],
            [sg.Text('Price Per Week of medications: $' + str(weeklycost))],
            [sg.Button('Exit')]
]


window = sg.Window('Pharm-Tracker', 
                   layout,
                   size = (1000, 750),
                   element_justification = "center",
                   resizable = True)



while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == 'Refresh':
        print("FUCK")
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Pill':
        # change the "output" element to be the value of "input" element
        pill_adder_button()

window.close()
