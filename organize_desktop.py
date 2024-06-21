import os
import shutil

# Define the paths
desktop_path = os.path.expanduser("~/Desktop")
pdf_folder = os.path.join(desktop_path, "PDFs")
image_folder = os.path.join(desktop_path, "Images")
others_folder = os.path.join(desktop_path, "Others")

# Create the folders if they do not exist
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)
os.makedirs(others_folder, exist_ok=True)

# Define file extensions
pdf_extensions = ['.pdf']
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']

# Move files to respective folders
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)
        if ext.lower() in pdf_extensions:
            shutil.move(file_path, pdf_folder)
        elif ext.lower() in image_extensions:
            shutil.move(file_path, image_folder)
        else:
            shutil.move(file_path, others_folder)

print("Desktop organized successfully!")
