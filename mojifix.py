import PySimpleGUI as Sg
import ftfy

Sg.theme("DarkBlue10")
layout = [[Sg.Text("Text to be fixed:"),
           Sg.Multiline(s=20, key="-unfixedText-", expand_x=True, expand_y=True), Sg.Button("Fix", key="-fix-")],
          [Sg.InputText(default_text='', s=20, key="-FixedText-", expand_x=True, expand_y=True, pad=(0, 0), readonly=True)]
          ],
window = Sg.Window("Mojifix, a simple text encoding fixer that uses ftfy", layout, size=(440, 400), resizable=True)

while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED:
        break
    if event == "-fix-":
        window["-FixedText-"].update(ftfy.fix_text(values["-unfixedText-"]))
window.close()
