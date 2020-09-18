import guizero as gz


class GUI:
    def __init__(self, user, case_number):
        self.user = user
        self.case_number = case_number
        self.app = gz.App(title="DSFP")
        self.main_window(self.app)




    def main_window(self, app):
        menubar = gz.MenuBar(self.app, toplevel=["File"], options=[[["New Case", self.new_case_popup], ["Exit", app.destroy]]])
        self.app.display()

    def new_case_popup(self):
        self.app.hide()
        new_case_window = gz.Window(self.app, title="Second window", height=200, width=200)
        name_label = gz.Text(new_case_window, text="Enter Name:")
        name_box = gz.TextBox(new_case_window)
        case_number_label = gz.Text(new_case_window, text="Case Number:")
        case_number_box = gz.TextBox(new_case_window)

    


        submit_button = gz.PushButton(new_case_window, text="Submit", command=lambda: self.set_case_info(name_box.value, str(case_number_box.value)))


    def set_case_info(self, user, caseno):
        self.app.show()



