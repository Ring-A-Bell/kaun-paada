import tkinter as tk
from tkinter import filedialog
from main import KaunPaada

class FilePickerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('File Picker')
        self.window.geometry('500x200')  # Set window size
        self.label = tk.Label(self.window, text='Welcome to Kaun Paada aka Who Farted?\nThis is a code smell detection tool')
        self.label.pack()
        self.button = tk.Button(self.window, text='Select File', command=self.select_file)
        self.button.pack()

    def select_file(self):
        filepath = filedialog.askopenfilename()
        print(f'Filepath selected: {filepath}')
        kaun_paada = KaunPaada(filepath)
        self.add_text(f'File selected: {filepath}')

    def add_text(self, text):
        # Create a new Label with the provided text
        new_label = tk.Label(self.window, text=text)
        # Add the new Label to the window
        new_label.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = FilePickerGUI()
    gui.run()