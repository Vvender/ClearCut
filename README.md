# ClearCut

ClearCut is a simple application for removing backgrounds from images using the rembg library.

## Overview

ClearCut provides a user-friendly interface built with PyQt5 to select a folder containing images and process them to remove their backgrounds. It utilizes the rembg library for background removal and integrates event handling for common actions like opening social media profiles or sending emails.

## Features

- Background removal from images in bulk.
- Intuitive GUI for easy navigation and interaction.
- Integration with social media profiles (GitHub, LinkedIn) and email.
- Error handling and logging for smooth user experience.

## Requirements

- Python 3.6 or higher
- PyQt5
- rembg
- PIL (Python Imaging Library)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/ClearCut.git
    cd ClearCut
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Click on "Select Folder" to choose the root folder containing images for background removal.

3. Once the folder is selected, click on "Start" to begin the background removal process.

4. Monitor the progress in the text area. Once completed, the processed images will be saved with "_reformed.png" suffix in the same directory.

## Contributing

Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the developers of PyQt5, rembg, and PIL for their excellent libraries.
