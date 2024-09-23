import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class MedicalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Sistema Médico Modular')
        self.setGeometry(100, 100, 400, 300)

        label = QLabel('Bem-vindo ao SMM', self)
        label.move(100, 150)

        self.show()

def main():
        app = QApplication(sys.argv)
        window = MedicalApp()
        sys.exit(app.exec())

if __name__ == '__main__':
        main()