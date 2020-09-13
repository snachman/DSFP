import guizero as gz


class GUI:
    def __init__(self, user, case_number):
        self.user = user
        self.case_number = case_number
        self.app = gz.App(title="DSFP")
        self.main_window(self.app)

    def set_case_info(self, user, case):
        self.user = user
        self.case_number = case
        print(user)


    def main_window(self, app):
        menubar = gz.MenuBar(self.app, toplevel=["File"], options=[[["New Case", self.popup], ["Exit", app.destroy]]])
        user_label = gz.Text(self.app, text=self.user)
        case_label = gz.Text(self.app, text=self.case_number)




        self.app.display()


    def popup(self):
        window = gz.Window(self.app, title="Second window")
        name_label = gz.Text(window, text="Enter Name:")
        name_box = gz.TextBox(window)
        case_number_label = gz.Text(window, text="Case Number:")
        case_number_box = gz.TextBox(window)


        submit_button = gz.PushButton(window, text="Submit", command=lambda: self.set_case_info(name_box.value, 22))




