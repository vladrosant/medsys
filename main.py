import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_window_controller import MainWindowController

def main():
    app = QApplication(sys.argv)
    main_window = MainWindowController()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
