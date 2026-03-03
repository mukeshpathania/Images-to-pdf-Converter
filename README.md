🖼️ Image to PDF Converter (Python)

A simple Python script that converts all images (.jpg, .jpeg, .png) from a folder into PDF format using the Pillow library.

📌 Project Description

This script:

Reads images from an images folder

Converts them into PDF format

Saves the converted files inside a pdf_files folder

Automatically creates the output folder if it does not exist

🚀 Features

✔ Batch image conversion
✔ Supports JPG, JPEG, and PNG formats
✔ Automatically creates output directory
✔ Simple and beginner-friendly code

🛠️ Technologies Used

Python 3

Pillow (Python Imaging Library)

OS Module

📂 Project Structure
project-folder/
│
├── image_to_PDF_Convert.py
├── images/              # Input images
└── pdf_files/           # Generated PDF files
⚙️ Installation
1️⃣ Install Python (if not installed)

Download from:
https://www.python.org/downloads/

2️⃣ Install Pillow
pip install pillow
▶️ How to Run

Place your images inside the images folder.

Run the script:

python image_to_PDF_Convert.py

Converted PDF files will be available inside the pdf_files folder.

💡 How It Works

The script checks if the output folder exists.

It loops through all files in the images folder.

If the file extension matches .jpg, .jpeg, or .png, it:

Opens the image

Converts it to RGB mode

Saves it as a .pdf file
