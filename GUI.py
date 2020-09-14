import guizero as gz


class GUI:
    def __init__(self):
        self.user = ""
        self.case_number = 0
        self.app = gz.App(title="DSFP", height=200, width=200)
        self.main_window(self.app)
        self.menubar = gz.MenuBar(toplevel=["File"], options=[[["New Case", self.new_case_popup], ["Case Info", self.see_case_info], ["Exit", app.destroy]]])

    def set_case_info(self, user, case):
        self.user = user
        self.case_number = case

    def see_case_info(self):
        case_info_window = gz.Window(self.app, title="Case Info")
        investigator_name_label = gz.Text(case_info_window, text=self.user)
        case_number_label = gz.Text(case_info_window, text=self.case_number)


    def main_window(self, app):
        name_label = gz.Text(self.app, text="Enter Name:")
        name_box = gz.TextBox(self.app)
        case_number_label = gz.Text(self.app, text="Case Number:")
        case_number_box = gz.TextBox(self.app)
        submit_button = gz.PushButton(self.app, text="Submit", command=lambda: self.new_case_popup(name_box.value, case_number_box.value))
        self.app.display()

    def new_case_popup(self, user, caseno):
        # self.app.hide()

        new_case_window = gz.Window(self.app, title="Second window", height=600, width=600, menubar=self.menubar)
        original_label = gz.Text(new_case_window, text="Original:")
        original_text_box = gz.TextBox(new_case_window)
        output_label = gz.Text(new_case_window, text="Output:")
        output_text_box = gz.TextBox(new_case_window)








