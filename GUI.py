import random
import tkinter as tk
from tkinter import filedialog

import pygame

from main import KaunPaada

GUI_TITLE = "Kaun Paada GUI"
GUI_DESCRIPTION = "Welcome to Kaun Paada aka Who Farted?\nThis is a code smell detection tool for Python\n\n"
HEADING_FONT = "Helvetica", 16, "bold"
SUBHEADING_FONT = "Helvetica", 14, "bold"
BODY_FONT = "Helvetica", 12, "normal"
SUPPORTED_FILE_TYPES = [("Python files", "*.py")]
AUDIO_FILES = ["assets/audio1.mp3", "assets/audio2.mp3", "assets/audio3.mp3"]


class FilePickerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.kaun_paada = None
        self.window.title('Kaun Paada GUI')
        self.window.geometry('1000x500')
        self.main_frame = tk.Frame(self.window)
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.my_canvas.yview)
        self.second_frame = tk.Frame(self.my_canvas)
        self.make_window_scrollable()
        self.add_text(GUI_DESCRIPTION, font=HEADING_FONT)
        self.add_text("Select a Python file to begin", font=BODY_FONT)
        self.add_button('Select File', self.select_file)

    def make_window_scrollable(self):
        self.main_frame.pack(fill=tk.BOTH, expand=1)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox('all')))

        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

    def select_file(self):
        filepath = filedialog.askopenfilename(filetypes=SUPPORTED_FILE_TYPES)
        print(f'Filepath selected: {filepath}')
        self.handle_callback(filepath)

    def handle_callback(self, filepath: str):
        self.kaun_paada = KaunPaada(filepath)
        # self.display_list_results(self.kaun_paada.long_method_detector(), "Long Methods Detected")
        self.display_dict_results(self.kaun_paada.long_method_detector(), "Long Classes Detected")
        # self.display_list_results(self.kaun_paada.long_parameter_list_detector(), "Long Parameter Lists Detected")
        self.display_dict_results(self.kaun_paada.long_parameter_list_detector(), "Long Functions Detected")
        duplicate_functions_list = self.kaun_paada.duplicate_code_detector()
        semantically_equal_functions_list = self.kaun_paada.semantic_code_detector()
        self.handle_duplicate_code(duplicate_functions_list, semantically_equal_functions_list)

    def handle_duplicate_code(self, duplicate_functions_list: list, semantically_equal_functions_list: list):
        if duplicate_functions_list or semantically_equal_functions_list:
            self.display_list_results(duplicate_functions_list, "Duplicate Functions based on Jaccard Similarity")
            self.display_list_results(semantically_equal_functions_list, "Semantically Equal Functions Detected")
            self.add_text("\nDuplicate Code has been detected. Do you want to refactor?", font=SUBHEADING_FONT)
            self.add_button('Save Refactored File', self.save_file)
        else:
            self.add_text("No duplicate code found!", font=SUBHEADING_FONT)
            self.add_text("No smells detected, so great job :)", font=HEADING_FONT)

    def display_list_results(self, results_list: list, text_label: str = "") -> None:
        self.add_text(text=text_label, font=SUBHEADING_FONT)
        if not results_list:
            self.add_text("None found! Congrats!")
            return
        self.play_random_audio()
        for item in results_list:
            self.add_text(item)
        self.add_text("\n--------------------------------------------\n")

    def display_dict_results(self, results_dict: dict, text_label: str = "") -> None:
        self.add_text(text_label, font=SUBHEADING_FONT)
        if not results_dict:
            self.add_text("None found! Congrats!")
            return
        self.play_random_audio()
        for key, value in results_dict.items():
            self.add_text(f"{key}\t\t----------> {value}")
        self.add_text("\n--------------------------------------------\n")

    @staticmethod
    def play_random_audio():
        audio_file = random.choice(AUDIO_FILES)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=SUPPORTED_FILE_TYPES)
        if filepath:
            self.kaun_paada.refactor_file(filepath)

    def add_text(self, text, font=BODY_FONT):
        new_label = tk.Label(self.second_frame, text=text, font=font)
        new_label.pack()

    def add_button(self, text, command, font=BODY_FONT):
        new_button = tk.Button(self.second_frame, text=text, command=command, font=font)
        new_button.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = FilePickerGUI()
    gui.run()
