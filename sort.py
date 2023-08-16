import os
import shutil

def sort_files(folder_location):

    def sorting(folder_name, file_types):
        for file_name in os.listdir(folder_location):

            # Check if there are files with the received extensions
            if file_name.endswith(file_types): 

                # Creating a Sortred folder if it doesn't exist
                sorted_folder = os.path.join(folder_location, "Sorted")
                os.makedirs(sorted_folder, exist_ok=True)   

                # Creating a folder for a category if it does not exist
                folder = os.path.join(sorted_folder, folder_name)
                os.makedirs(folder, exist_ok=True)

                # Moving files to a folder
                file_path = os.path.join(folder_location, file_name)
                shutil.move(file_path, folder)

    
    # Sorting Images
    sorting("Images", (".png", ".jpg", ".bmp", ".gif", ".tif", ".kra", ".svg",
                        ".raw.", ".tiff", ".psd", ".bmp", ".jpeg", ".webp"))