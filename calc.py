import PySimpleGUI as sg

def plus(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x , y):
    return x / y

numx = 0
numy = 0

layout = [[sg.Text(size=(20,1), key='-Output-')], 
        [sg.Button(button_text=' + ', size=(3,3), font=('Any 15')), sg.Button(button_text=' - ', size=(3,3), font=('Any 15')),
        sg.Button(button_text=' X ', size=(3,3), font=('Any 15')), sg.Button(button_text=' / ', size=(3,3), font=('Any 15'))],
        [sg.Button(button_text=' 9 '), sg.Button(button_text=' 8 '), sg.Button(button_text=' 7 '), sg.Button(button_text=' 6 ')]]

window = sg.Window("Calculator", layout)
while True:
    event, values = window.read()
    print(event, values)
    if(event == sg.WIN_CLOSED):
        break

window.close()