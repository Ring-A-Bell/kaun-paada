import tkinter as tk
from tkinter import filedialog
from main import KaunPaada

GUI_TITLE = "Kaun Paada GUI"
GUI_DESCRIPTION = "Welcome to Kaun Paada aka Who Farted?\nThis is a code smell detection tool for Python\n\n"
HEADING_FONT = "Helvetica", 16, "bold"
SUBHEADING_FONT = "Helvetica", 14, "bold"
BODY_FONT = "Helvetica", 12, "normal"
SUPPORTED_FILE_TYPES = [("Python files", "*.py")]

class FilePickerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.kaun_paada = None
        self.window.title('Kaun Paada GUI')
        self.window.geometry('1000x500')  # Set window size
        self.add_text(GUI_DESCRIPTION, font=HEADING_FONT)
        self.add_text("Select a Python file to begin", font=BODY_FONT)
        self.add_button('Select File', self.select_file)

    def select_file(self):
        filepath = filedialog.askopenfilename(filetypes=SUPPORTED_FILE_TYPES)
        print(f'Filepath selected: {filepath}')
        self.handle_callback(filepath)

    def handle_callback(self, filepath: str):
        self.kaun_paada = KaunPaada(filepath)
        self.display_results(self.kaun_paada.long_method_detector(), "Long Methods Detected")
        self.display_results(self.kaun_paada.long_parameter_list_detector(), "Long Parameter Lists Detected")
        if self.kaun_paada.duplicate_code_detector():
            self.add_text("Duplicate Code has been detected. Do you want to refactor?", font=SUBHEADING_FONT)
            self.add_button('Save Refactored File', self.save_file)
        else:
            self.add_text("No duplicate code found!", font=SUBHEADING_FONT)
            self.add_text("No smells detected, so great job :)", font=HEADING_FONT)

    def display_results(self, results_list: list, text_label: str = "") -> None:
        self.add_text(text=text_label, font=SUBHEADING_FONT)
        if not results_list:
            self.add_text("None found! Congrats!")
            return
        for item in results_list:
            self.add_text(item)
        self.add_text("\n--------------------------------------------\n")

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=SUPPORTED_FILE_TYPES)
        if filepath:
            self.kaun_paada.refactor_file(filepath)

    def add_text(self, text, font=BODY_FONT):
        new_label = tk.Label(self.window, text=text, font=font)
        new_label.pack()

    def add_button(self, text, command, font=BODY_FONT):
        new_button = tk.Button(self.window, text=text, command=command, font=font)
        new_button.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = FilePickerGUI()
    gui.run()
