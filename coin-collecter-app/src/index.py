from tkinter import Tk
from ui.ui import UI


def main():
    """sets up and launches the main app window"""
    window = Tk()
    window.title("Coin Collector Game")
    window.geometry("1200x600")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()