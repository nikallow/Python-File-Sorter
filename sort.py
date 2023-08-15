import os
import shutil
import main

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

    # Creating folders
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