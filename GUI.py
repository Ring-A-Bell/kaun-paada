import tkinter as tk
from tkinter import filedialog
from main import KaunPaada


class FilePickerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.kaun_paada = None
        self.window.title('File Picker')
        self.window.geometry('500x200')  # Set window size
        self.label = tk.Label(self.window, text='Welcome to Kaun Paada aka Who Farted?\nThis is a code smell '
                                                'detection tool')
        self.label.pack()
        self.button = tk.Button(self.window, text='Select File', command=self.select_file)
        self.button.pack()

    def select_file(self):
        filepath = filedialog.askopenfilename()
        print(f'Filepath selected: {filepath}')
        self.kaun_paada = KaunPaada(filepath)
        for item in self.kaun_paada.long_method_detector():
            self.add_text(item)
        self.add_text("--------------------------------------------\n")
        for item in self.kaun_paada.long_parameter_list_detector():
            self.add_text(item)
        self.button = tk.Button(self.window, text='Save File', command=self.save_file)
        self.button.pack()

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".py",
                                                filetypes=[("Python File", "*.py"), ("All Files", "*.*")])
        if filepath:
            self.kaun_paada.refactor_file(filepath)

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
