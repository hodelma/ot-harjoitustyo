from tkinter import Label

class UI:
    """main ui class for the app"""

    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._initialize()

    def _initialize(self):
        label = Label(self._root, text="Welcome to Coin Collector Game!")
        label.pack()