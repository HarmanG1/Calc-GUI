import PySimpleGUI as sg

expr = []

layout = [[sg.Text(size=(10,1))],
        [sg.Text(size=(16,1), key='-Output-', font=('Any 18'), text_color='black')],
        [sg.Text(size=(10,1))],
        [sg.ReadFormButton(button_text='C', size=(5,2)), sg.Button(button_text='DEL', size=(5,2))], 
        [sg.Button(button_text=' + ', size=(5,2)), sg.Button(button_text=' - ', size=(5,2)),
        sg.Button(button_text=' * ',  size=(5,2)), sg.Button(button_text=' / ',  size=(5,2))],
        [sg.Button(button_text='6',  size=(5,2)), sg.Button(button_text='7',  size=(5,2)),
        sg.Button(button_text='8',  size=(5,2)), sg.Button(button_text='9',  size=(5,2))],
        [sg.Button(button_text='2',  size=(5,2)), sg.Button(button_text='3',  size=(5,2)),
        sg.Button(button_text='4',  size=(5,2)), sg.Button(button_text='5',  size=(5,2))],
        [sg.Button(button_text='0',  size=(5,2)), sg.Button(button_text='1',  size=(5,2)),
        sg.Button(button_text='.',  size=(5,2)), sg.Button(button_text=' = ',  size=(5,2))]]

window = sg.Window("Calculator", layout)
while True:
    event, value = window.read()
    if(event == sg.WIN_CLOSED):
        break
    elif(event == 'C'):
        expr.clear()
        window['-Output-'].update(''.join(expr))
    elif(event == 'DEL'):
        expr.pop(len(expr) - 1)
        window['-Output-'].update(''.join(expr))
    elif(event == ' = '):
        total = eval(''.join(expr))
        expr.clear()
        expr.append(str(total))
        window['-Output-'].update(total)
    elif(len(expr) == 17):
        pass
    else:
        expr.append(event)
        window['-Output-'].update(''.join(expr))
    
window.close()
