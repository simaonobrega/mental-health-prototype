import tkinter as tk


class AnalyserScreen(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        self.input_data = None
        self.title("Analyser")
        self._setup_ui()

    def _setup_ui(self):
        pass

    def _load_data(self, data_source):
        pass

    def _present_analysis(self):
        pass

    def _set_period_of_analysis(self):
        pass

    def _set_ai_parameter(self):
        pass

    def _request_alternative_feedback(self):
        pass
