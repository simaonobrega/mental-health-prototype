import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class RegisterFeelingScreen(tk.Toplevel):
    FONT_LARGE = ('Helvetica', '16')
    BUTTON_BG_COLOR = 'blue'
    BUTTON_FG_COLOR = 'white'

    def __init__(self, parent, controller, title="Register Feeling"):
        super().__init__(parent)
        self._controller = controller
        self.title(title)
        self._selected_emoji = None
        self._emotion_factory = self._controller.emotion_factory_requested()

        self._setup_date_selector()
        self._setup_emoji_selector()
        self._setup_text_entry()
        self._setup_submit_button()

    def _setup_date_selector(self):
        date_label = ttk.Label(self, text="Date:")
        date_label.pack(fill=tk.X)
        self._date_entry = DateEntry(self)
        self._date_entry.pack(fill=tk.X)

    def _setup_emoji_selector(self):
        self._emojis = self._emotion_factory.get_all_emojis()
        emoji_label = ttk.Label(self, text="Select Your Mood:")
        emoji_label.pack(fill=tk.X)
        self.emoji_frame = ttk.Frame(self)
        self.emoji_frame.pack(fill=tk.X)
        self._create_emoji_buttons()

    def _setup_text_entry(self):
        text_label = ttk.Label(self, text="Your Thoughts:")
        text_label.pack(fill=tk.X)
        self.text_entry = tk.Text(self, height=5, width=30)
        self.text_entry.pack(fill=tk.X, pady=10)

    def _setup_submit_button(self):
        submit_button = tk.Button(self, text="Submit",
                                  command=self._submit)
        submit_button.pack(fill=tk.X, pady=10)

    def _submit(self):
        self._controller.on_submit_feeling_button()

        # Close window
        self.destroy()

    def _create_emoji_buttons(self):
        self._emoji_buttons = {}
        for emotion_name, emoji in self._emojis.items():
            emoji_button = tk.Button(self.emoji_frame, text=emoji,
                                     font=self.FONT_LARGE,
                                     command=lambda
                                         n=emotion_name: self._select_feeling(
                                         n))
            emoji_button.pack(side=tk.LEFT)
            self._emoji_buttons[emotion_name] = emoji_button

    def _select_feeling(self, feeling_name):
        if self._selected_emoji:
            self._selected_emoji.config(bg='SystemButtonFace', fg='black')
        selected_button = self._emoji_buttons[feeling_name]
        selected_button.config(bg=self.BUTTON_BG_COLOR, fg=self.BUTTON_FG_COLOR)
        self._selected_emoji = selected_button
