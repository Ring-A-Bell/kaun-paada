import PySimpleGUI as gui

gui.theme('Dark')
layout = [[gui.Text('Sample text on Row 1')],
          [gui.Text('Enter any text'), gui.InputText()],
          [gui.Button('Print to Console'), gui.Button('Exit')]]

# Window creation
window = gui.Window('Kaun Paada: Code Smell Detector', layout)
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Exit':
        break
    print(f'Text entered via the GUI: {values[0]}')

window.close()