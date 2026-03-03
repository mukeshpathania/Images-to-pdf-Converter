import os
from PIL import Image

input_folder = "images"
output_folder = "pdf_files"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg",".jpeg",".png")):
        img_path = os.path.join(input_folder,filename)
        img = Image.open(img_path).convert("RGB")

        new_filename = os.path.splitext(filename)[0] + ".pdf"
        pdf_file_path = os.path.join(output_folder,new_filename)
        img.save(pdf_file_path)

print("All images have been converted to PDF")
