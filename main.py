import os
import shutil
from tkinter import filedialog
import customtkinter as ctk
import webbrowser

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("File sorter")
        self.geometry("400x240")
        self.resizable(False, False)
        my_font = ctk.CTkFont("Roboto Medium", 14)


        # Configure folder entry
        self.folder_entry = ctk.CTkEntry(master=self,width=360, height=40)
        self.folder_entry.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))
        self.folder_entry.configure(placeholder_text="Enter the folder location",
                                     font=my_font)


        # Button frame
        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, padx=(20, 20), pady=(10, 80))

        # Folder button
        self.folder_button = ctk.CTkButton(master=self.button_frame)
        self.folder_button.grid(row=1, column=0, padx=(0, 10), pady=(10, 0))
        self.folder_button.configure(width=170, height=40, text="Choose folder",
                                      font=my_font, command=self.select_folder)

        # Sort button
        self.sort_button = ctk.CTkButton(master=self.button_frame)
        self.sort_button.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))
        self.sort_button.configure(width=170, height=40, text="Sort files",
                                      font=my_font)# , command=self.sort_files)


        # Additional buttons frame
        self.add_button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.add_button_frame.grid(row=2, column=0, padx=(20, 20), pady=(0,10))

        # Github button
        self.github_button = ctk.CTkButton(master=self.add_button_frame)
        self.github_button.grid(row=1, column=0, padx=(0, 80), pady=(0, 10))
        self.github_button.configure(width=100, height=30, text="GitHub",
                                      font =my_font, command=self.github_link)

        # Appearance_changer
        self.appearance_changer = ctk.CTkOptionMenu(self.add_button_frame,
                                                    values=["System", "Dark", "Light"])
        self.appearance_changer.grid(row=1, column=1, padx=(80,0), pady = (0,10))
        self.appearance_changer.configure(width=100, height=30, font =my_font,
                                           command = self.change_appearance_mode_event)


    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder_path)



    def github_link(self):
        link = "https://github.com/nikallow/File-Sorter"
        webbrowser.open(link)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()