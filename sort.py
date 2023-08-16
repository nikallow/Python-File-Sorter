import os
import shutil

def sort_files(folder_location):

    def sorting(folder_name, file_types):
        for file_name in os.listdir(folder_location):

            # Check if there are files with the received extensions
            if file_name.endswith(file_types): 

                # Creating a Sorted folder if it doesn't exist
                sorted_folder = os.path.join(folder_location, "Sorted")
                os.makedirs(sorted_folder, exist_ok=True)   

                # Creating a folder for a category if it does not exist
                folder = os.path.join(sorted_folder, folder_name)
                os.makedirs(folder, exist_ok=True)

                # Get the base name and extension of the file
                base_name, extension = os.path.splitext(file_name)

                # Check if the file already exists in the destination folder
                new_file_name = file_name
                suffix = 0
                while os.path.exists(os.path.join(folder, new_file_name)):
                    suffix += 1
                    new_file_name = f"{base_name} ({suffix}){extension}"

                # Moving files to the folder with the updated file name
                file_path = os.path.join(folder_location, file_name)
                new_file_path = os.path.join(folder, new_file_name)
                shutil.move(file_path, new_file_path)
    
    # Sorting Images
    sorting("Images", (".png", ".jpg", ".bmp", ".gif", ".tif", ".kra", ".svg",
                        ".raw.", ".tiff", ".psd", ".bmp", ".jpeg", ".webp"))