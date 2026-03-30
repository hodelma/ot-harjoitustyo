from tkinter import ttk

class UI:
    """main ui class for the app"""
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(
            master=self._root,
            text="Welcome to Coin Collector Game!"
        )
        label.pack()