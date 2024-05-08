# background_remover.py

from ExceptionHandler.exception_handler import CustomExceptionHandler
from rembg import remove
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog


class BackgroundRemover:
    def __init__(self, app, ui):
        # Initialize BackgroundRemover object with the application and UI
        self.app = app
        self.ui = ui
        self.root_folder = None
        self.processed_files = 0
        self.total_files = 0

    def set_root_folder(self):
        try:
            # Open a dialog to select the root folder
            root_folder = filedialog.askdirectory(title="Select the root folder")
            if root_folder:
                # Set the selected folder as the root folder and update UI
                self.root_folder = root_folder
                self.ui.lbl_file_location.setText(root_folder)
        except Exception as e:
            # Handle exceptions during folder selection
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred during selecting file location, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()

    def remove_background(self, input_path, output_path):
        try:
            # Open input image, remove background, and save the output
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            background = Image.new("RGBA", input_image.size, (0, 0, 0, 0))
            background.paste(output_image, (0, 0), output_image)
            output_filename = os.path.splitext(os.path.basename(output_path))[0] + "_reformed.png"
            output_path = os.path.join(os.path.dirname(output_path), output_filename)
            background.save(output_path, format="PNG")

        except Exception as e:
            # Handle exceptions during background removal
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred during removing image background, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()

    def process_images(self):
        try:
            # Disable buttons during image processing
            self.ui.btn_start.setEnabled(False)
            self.ui.btn_file_location.setEnabled(False)
            # Get total number of JPEG files
            self.total_files = sum(len(files) for _, _, files in os.walk(self.root_folder) if
                                   any(file.lower().endswith((".jpg", ".jpeg")) for file in files))

            # Reset processed files count
            self.processed_files = 0

            if self.root_folder:
                for root, _, files in os.walk(self.root_folder):
                    for file in files:
                        if file.lower().endswith((".jpg", ".jpeg")):
                            self.processed_files += 1  # Increment processed files count
                            input_path = os.path.join(root, file)
                            output_path = os.path.join(root, os.path.splitext(file)[0] + "_reformed.png")
                            self.remove_background(input_path, output_path)
                            progress_text = f"Processing: {self.processed_files}/{self.total_files}\n{input_path}\n"
                            print(progress_text)  # Print to console
                            self.ui.txt_progress.append(progress_text)  # Append to txt_progress widget
            else:
                self.ui.txt_progress.append("Root folder not set.")

        except Exception as e:
            # Handle exceptions during image processing
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred during removing image processing, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()
