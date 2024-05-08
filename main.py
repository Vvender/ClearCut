# main.py

from ExceptionHandler.exception_handler import CustomExceptionHandler
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from Gui.ui_clearcut import Ui_ClearCut
from EventHandler.event_handler import EventHandler
from BackgroundRemover.background_remover import BackgroundRemover


class BackgroundThread(QThread):
    # Signal emitted when the background task is finished
    finished = pyqtSignal()

    def __init__(self, background_remover):
        super().__init__()
        self.background_remover = background_remover

    def run(self):
        # Start processing images
        self.background_remover.process_images()
        # Emit signal indicating completion
        self.finished.emit()


class MainWindow:
    def __init__(self):
        # Initialize the Qt application
        self.app = QApplication(sys.argv)
        # Create the main window
        self.ui_window = QWidget()
        # Set up the UI using the ClearCut UI
        self.ui = Ui_ClearCut()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Initialize event handler and background remover
        self.event_handler = EventHandler(self.app, self.ui)
        self.background_remover = BackgroundRemover(self.app, self.ui)

        # Connect main button events
        self.ui.btn_github.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # Connect background removing buttons event
        self.ui.btn_file_location.clicked.connect(self.background_remover.set_root_folder)
        self.ui.btn_start.clicked.connect(self.start_background_task)

    def start_background_task(self):
        try:
            # Check if a root folder is selected
            if self.background_remover.root_folder:
                # Create a background thread and connect its finished signal
                self.background_thread = BackgroundThread(self.background_remover)
                self.background_thread.finished.connect(self.on_background_task_finished)
                self.background_thread.start()
            else:
                # Display a message if no root folder is selected
                self.ui.txt_progress.append("Please select the root folder first.")
        except Exception as e:
            # Handle exceptions during background task start
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred while starting the background task, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()

    def on_background_task_finished(self):
        try:
            # Update progress text and enable buttons after task completion
            self.ui.txt_progress.append("All images processed successfully.")
            self.ui.txt_progress.append(
                f"Processed files: {self.background_remover.processed_files} / {self.background_remover.total_files}")
            self.ui.btn_start.setEnabled(True)
            self.ui.btn_file_location.setEnabled(True)
        except Exception as e:
            # Handle exceptions during background task completion
            custom_exception = CustomExceptionHandler(e)
            print(
                f"An error occurred while finishing the background task, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            self.close_connection()


if __name__ == "__main__":
    # Start the main application
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
