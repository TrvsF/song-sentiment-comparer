import PySimpleGUI as simplegui

simplegui.theme("DarkPurple4")

# 1- the layout
layout = [
    [simplegui.Text("SongSentimentComparer")],
    [simplegui.Input("song name...", key="songinput")],
    [simplegui.Button("enter")],
    [simplegui.Text(key="output")]
]

# 2 - the window
window = simplegui.Window("SongSentimentComparer", layout, size=(640, 480), element_justification="c", finalize=True)
window["songinput"].bind("<Return>", "sireturn")

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)    

    if event == simplegui.WIN_CLOSED:
        break

    if event == "Show":
        window["output"].update(values["songinput"])

    if event == "sireturn" + "songinput" or "enter":
        print(values["songinput"])

    if window.find_element_with_focus() == window["songinput"]:
        print("a")