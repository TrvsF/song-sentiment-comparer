import PySimpleGUI as simplegui

simplegui.theme("DarkPurple4")

# 1- the layout
layout = [
    [
        simplegui.Text("SongSentimentComparer"),
    ],
    [simplegui.Input(key='songinput')],
    [simplegui.Button('Show'), simplegui.Button('Exit')],
    [simplegui.Text(key="output")]
]

# 2 - the window
window = simplegui.Window("SongSentimentComparer", layout, size=(640, 480), element_justification='c')

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == simplegui.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window["output"].update(values["songinput"])