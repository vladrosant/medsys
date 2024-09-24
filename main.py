import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_window_controller import MainWindowController
from controllers.add_patient_controller import AddPatientController

def main():
    app = QApplication(sys.argv)
    main_window = MainWindowController()
    window = AddPatientController()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
