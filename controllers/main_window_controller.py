from PyQt6.QtWidgets import QWidget, QLabel

class MainWindowController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Medical System - Main Window')
        self.setGeometry(100, 100, 600, 400)

        label = QLabel('Medical System Dashboard', self)
        label.move(200, 200)

        self.show()
