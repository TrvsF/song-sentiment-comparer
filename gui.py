import dearpygui.dearpygui as dpg

class Gui(object): # whats the object for?


    def __init__(self) -> None:
        print("starting gui")

        dpg.create_context()
        dpg.create_viewport(title='songsentimentfinder', width=800, height=600)
        dpg.setup_dearpygui()

        with dpg.window(label="Example Window"):
            dpg.add_text("enter thing below")
            dpg.add_input_text(label="string", callback=self.input_updated)
            dpg.add_button(label="Save", callback=self.search_clicked)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def search_clicked(self): # passing the self is stupid
        print("Save Clicked")

    def input_updated(self):
        print("typey typey")
    
gui = Gui()