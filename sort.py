import os
import shutil

def sort_files(folder_location):
    sorted_folder = os.path.join(folder_location, "Sorted")
    os.makedirs(sorted_folder, exist_ok=True)

    images_folder = os.path.join(sorted_folder, "Images")
    os.makedirs(images_folder, exist_ok=True)

    for file_name in os.listdir(folder_location):
        if file_name.endswith((".png", ".jpg", ".bmp", ".gif", ".tif",
                              ".kra", ".svg", ".raw.", ".tiff", ".psd",
                              ".bmp", ".jpeg", ".webp")):
            file_path = os.path.join(folder_location, file_name)
            shutil.move(file_path, images_folder)