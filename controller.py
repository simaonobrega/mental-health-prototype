from model import Model
from view import View


class Controller:
    def __init__(self):
        # Initialize the remaining MVC paradigm components
        model = Model()
        view = View(controller=self, model=model)
        view.open_main_screen()

    def start_program(self):
        print("program starting")
