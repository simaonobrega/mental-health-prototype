import tkinter as tk


class StatsScreen(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        self.title("Data Analyser")

        self._setup_ui()

    def _setup_ui(self):
        pass

    def _load_data(self):
        pass

    def _visualize_data(self):
        pass

