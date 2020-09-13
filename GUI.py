import guizero as gz


def main_window():
    app = gz.App(title="DSFP")
    menubar = gz.MenuBar(app, toplevel=["File"], options=[[["New Case", popup()]]])




    app.display()


def popup():
    print("test")
