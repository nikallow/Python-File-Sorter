import os
import shutil

def sort_files(folder_location):

    def sorting(folder_name, file_types):    
        folder = os.path.join(sorted_folder, folder_name)
        os.makedirs(folder, exist_ok=True)

        for file_name in os.listdir(folder_location):
            if file_name.endswith(file_types):
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, folder)

    # Creating a Sortred folder
    sorted_folder = os.path.join(folder_location, "Sorted")
    os.makedirs(sorted_folder, exist_ok=True)   

    # Sorting Images
    sorting("Images", (".png", ".jpg", ".bmp", ".gif", ".tif", ".kra", ".svg",
                        ".raw.", ".tiff", ".psd", ".bmp", ".jpeg", ".webp"))