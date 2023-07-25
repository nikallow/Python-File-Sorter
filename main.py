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
                                      font=my_font , command=self.sort_files)
        

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

    # Sorting files
    def sort_files(self):
        self.info_label.configure(text=" ")
        folder_location = app.folder_entry.get()

        if folder_location == "":
            self.info_label.configure(text="Please select a folder.")
            return

        if not os.path.exists(folder_location):
            self.info_label.configure(text="The specified folder does not exist.")
            return

        # Create folders
        sorted_folder = os.path.join(folder_location, "Sorted")
        os.makedirs(sorted_folder, exist_ok=True)

        images_folder = os.path.join(sorted_folder, "Images")
        os.makedirs(images_folder, exist_ok=True)

        documents_folder = os.path.join(sorted_folder, "Documents")
        os.makedirs(documents_folder, exist_ok=True)

        archives_folder = os.path.join(sorted_folder, "Archives")
        os.makedirs(archives_folder, exist_ok=True)

        videos_folder = os.path.join(sorted_folder, "Videos")
        os.makedirs(videos_folder, exist_ok=True)

        # Sorting files
        for file_name in os.listdir(folder_location):
            # Images
            if file_name.endswith((".png", ".jpg", ".bmp", ".gif", ".tif",
                                    ".kra", ".svg", ".raw.", ".tiff", ".psd",
                                    ".bmp", ".jpeg", ".webp")):
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, images_folder)

            # Documents
            if file_name.endswith((".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
                                    ".pdf", ".djvu", ".fb2", ".epub", ".mobi", ".txt",
                                    ".odt", ".ods", ".odp", ".odg", ".odf", ".odb")):
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, documents_folder)

            # Archives
            if file_name.endswith((".zip", ".7z", ".rar", ".tar", ".gz", ".tar.gz")):
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, archives_folder)

            # Videos
            if file_name.endswith((".mp4", ".mkv", ".mov", ".hevc")):
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, videos_folder)

        # Show a success message
        self.info_label.configure(text="Files sorted successfully")


if __name__ == "__main__":
    app = App()
    app.mainloop()