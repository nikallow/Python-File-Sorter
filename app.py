import os
import customtkinter as ctk
from tkinter import filedialog
import webbrowser

from sort import sort_files


class InfoWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)

        # Configure window
        self.title("Information")
        self.geometry("240x200")
        self.resizable(False, False)

        # Fonts
        small_font = ctk.CTkFont("Roboto Medium", 12)
        medium_font = ctk.CTkFont("Roboto Medium", 16)
        large_font = ctk.CTkFont("Roboto Medium", 24)

        # Frame
        self.frame = ctk.CTkFrame(self, width= 200, height = 160)
        self.frame.grid(padx = 20, pady = 20)

        # Program name
        self.program_label = ctk.CTkLabel (master=self.frame, font=large_font,
                                            width=200, height=30,
                                            anchor="center",
                                            text="File sorter")
        self.program_label.grid(row=0, column=0)

        # Version
        self.version_label = ctk.CTkLabel (master=self.frame, font=small_font,
                                            width=200, height=30,
                                            anchor="center",
                                            text="Version: dev build")
        self.version_label.grid(row=1, column=0)

        # Author
        self.author_label = ctk.CTkLabel (master=self.frame, font=medium_font,
                                           width=200, height=30,
                                           anchor="center",
                                           text="nikallow © 2023")
        self.author_label.grid(row=2, column=0)

        # License
        self.license_label = ctk.CTkLabel (master=self.frame, font=medium_font,
                                            width=200, height=30,
                                            anchor="center",
                                            text="License: GPL v3?")
        self.license_label.grid(row=3, column=0)

        # GitHub
        self.github_button = ctk.CTkButton(master=self.frame, font=medium_font,
                                           width= 160, height=30,
                                           anchor="center",
                                           text="Source code",
                                           command=self.github_link)
        self.github_button.grid(row=4, column=0, pady=4)


    # Opening a link to the repository
    def github_link(self):
        link = "https://github.com/nikallow/Python-File-Sorter"
        webbrowser.open(link)
        


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
        self.folder_entry.configure(font=my_font, placeholder_text =
                                     "Enter the folder location")


        # Button frame
        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, padx=20, pady=10)

        # Folder button
        self.folder_button = ctk.CTkButton(master=self.button_frame,
                                            width=175, height=40)
        self.folder_button.grid(row=1, column=0)
        self.folder_button.configure(text="Choose folder", font=my_font, 
                                     command=self.select_folder)

        # Sort button
        self.sort_button = ctk.CTkButton(master=self.button_frame,
                                         width=175, height=40)
        self.sort_button.grid(row=1, column=1, padx=(10, 0))
        self.sort_button.configure(font=my_font, text="Sort files",
                                    command=self.sort_files)
        

        # Info frame
        self.info_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.info_frame.grid(row=2, column=0, padx=20)

        # Info label
        self.info_label = ctk.CTkLabel(master=self.info_frame,
                                       width=360, height=30,
                                       text=" ", font=my_font)
        self.info_label.grid(row=0, column=0)        


        # Additional buttons frame
        self.add_button_frame = ctk.CTkFrame(master=self, 
                                             fg_color="transparent")
        self.add_button_frame.grid(row=3, column=0, padx=20, pady=(50, 10))

        # Github button
        self.info_button = ctk.CTkButton(master=self.add_button_frame)
        self.info_button.grid(row=1, column=0)
        self.info_button.configure(font=my_font, width=100, height=30, 
                                    text="Info", command=self.open_info)

        # Appearance_changer
        self.appearance_changer = ctk.CTkOptionMenu(self.add_button_frame,
                                                    values=["System", "Dark", 
                                                            "Light"])
        self.appearance_changer.grid(row=1, column=1, padx=(160,0))
        self.appearance_changer.configure(font=my_font, width=100, height=30,
                                          command = 
                                           self.change_appearance_mode_event)
        
    # Selecting a folder
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder_path)
        self.info_label.configure(text=" ")


    # Change theme
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


    # Open Info Window
    def open_info(self):
        info_window = InfoWindow(self)
        info_window.transient(self)
        info_window.after(100, info_window.focus_set)
        self.wait_window(info_window)


    # Sorting files
    def sort_files(self):
        self.clear_info_label()
        folder_location = self.folder_entry.get()

        if folder_location == "":
            self.info_label.configure(text="Please select a folder.")
            return

        if not os.path.exists(folder_location):
            self.info_label.configure(text=
                                      "The specified folder does not exist.")
            return

        sort_files(folder_location)

        # Disable the sort button and show a success message
        self.change_button_state(self.sort_button, "disabled")
        self.info_label.configure(text="Files sorted successfully")

        # Enable the sort button and clear info label
        self.after(1500, self.clear_info_label)
        self.after(1500, self.change_button_state, self.sort_button, "enabled")


    # Clear info label
    def clear_info_label(self):
        self.info_label.configure(text=" ")


    # Change button state
    def change_button_state(self, button, state):
        button.configure(state=state)