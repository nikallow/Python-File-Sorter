# Copyright 2023 nikallow

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import os
import shutil
from tkinter import filedialog
import customtkinter as ctk
import webbrowser

import sort


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


        # Folder entry
        self.folder_entry = ctk.CTkEntry(master=self,width=360, height=40)
        self.folder_entry.grid(row=0, column=0, padx=20, pady=(20, 0))
        self.folder_entry.configure(placeholder_text="Enter the folder location",
                                     font=my_font)


        # Button frame
        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, padx=20, pady=(10))

        # Folder button
        self.folder_button = ctk.CTkButton(master=self.button_frame,
                                            width=175, height=40)
        self.folder_button.grid(row=1, column=0, padx=(0, 5), pady=0)
        self.folder_button.configure( text="Choose folder", font=my_font, 
                                     command=self.select_folder)

        # Sort button
        self.sort_button = ctk.CTkButton(master=self.button_frame,
                                         width=175, height=40)
        self.sort_button.grid(row=1, column=1, padx=(5, 0), pady=0)
        self.sort_button.configure( text="Sort files",
                                      font=my_font , command=self.sort.sort_files)
        

        # Info frame
        self.info_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.info_frame.grid(row=2, column=0, padx=20, pady=(0, 50))

        # Info label
        self.info_label = ctk.CTkLabel(master=self.info_frame,
                                       width=360, height=30,
                                       text=" ", font=my_font)
        self.info_label.grid(row=0, column=0, padx=0, pady=0)        


        # Additional buttons frame
        self.add_button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.add_button_frame.grid(row=3, column=0, padx=(20, 20), pady=(0,10))

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

    # Selecting a folder
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder_path)
        self.info_label.configure(text=" ")

    # Opening a link to the repository
    def github_link(self):
        link = "https://github.com/nikallow/Python-File-Sorter"
        webbrowser.open(link)

    # Change theme
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()