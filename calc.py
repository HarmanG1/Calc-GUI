import PySimpleGUI as sg #Importing the library 

expr = [] #Creating list to hold the expression 

#Setting up the layout of the window with the output line as well as the buttons 
layout = [[sg.Text(size=(16,1), key='-Output-', font=('Any 18'), text_color='black')],
        [sg.ReadFormButton(button_text='C', size=(5,2)), sg.Button(button_text='DEL', size=(5,2))], 
        [sg.Button(button_text=' + ', size=(5,2)), sg.Button(button_text=' - ', size=(5,2)),
        sg.Button(button_text=' * ',  size=(5,2)), sg.Button(button_text=' / ',  size=(5,2))],
        [sg.Button(button_text='6',  size=(5,2)), sg.Button(button_text='7',  size=(5,2)),
        sg.Button(button_text='8',  size=(5,2)), sg.Button(button_text='9',  size=(5,2))],
        [sg.Button(button_text='2',  size=(5,2)), sg.Button(button_text='3',  size=(5,2)),
        sg.Button(button_text='4',  size=(5,2)), sg.Button(button_text='5',  size=(5,2))],
        [sg.Button(button_text='0',  size=(5,2)), sg.Button(button_text='1',  size=(5,2)),
        sg.Button(button_text='.',  size=(5,2)), sg.Button(button_text=' = ',  size=(5,2))]]

sg.theme("Dark Amber")
window = sg.Window("Calculator", layout) #Creating the GUI window 

while True:
    event, value = window.read() #Holding the values passed in from reading the window
    if(event == sg.WIN_CLOSED): #Checks if the user has closed the window 
        break
    elif(event == 'C'): #Checks if user has pressed clear 
        expr.clear() #Empties the list
        window['-Output-'].update(''.join(expr)) #Clears the output line 
    elif(event == 'DEL'): #Checks if user pressed delete 
        if len(expr) > 0: #Checks if list is empty before poping an element
            expr.pop(len(expr) - 1)
        window['-Output-'].update(''.join(expr))
    elif(event == ' = '): #Checks if user pressed =
        total = eval(''.join(expr)) #Evaluates the expression by joining all elements of the list 
        expr.clear() #Clears the list
        expr.append(str(total)) #Adds the new value to the list 
        window['-Output-'].update(total)
    elif(len(expr) == 17): #Checks for overall expr lenght limit
        pass
    else: #Else a num button or expr button has been pressed
        expr.append(event) #Add the new expr element to the list
        window['-Output-'].update(''.join(expr))
    
window.close() #Close the window when finished
