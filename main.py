import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_window_controller import MainWindowController
from controllers.add_patient_controller import AddPatientController
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Grid Layout Widget
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 230, 341, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Username label
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        # Password label
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        # Horizontal layout for password input and show button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Password input field
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        # Show password button
        self.show_password = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.show_password.setObjectName("show_password")
        self.horizontalLayout.addWidget(self.show_password)

        # Add horizontal layout to the grid
        self.gridLayout.addLayout(self.horizontalLayout, 2, 3, 1, 1)

        # Username input field
        self.lineEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)

        # Spacer between fields
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 2)

        # Horizontal layout for buttons
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 330, 341, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Sign-up button
        self.sign_up = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.sign_up.setObjectName("sign_up")
        self.horizontalLayout_2.addWidget(self.sign_up)

        self.recover_password = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.recover_password.setObjectName("recover_password")
        self.horizontalLayout_2.addWidget(self.recover_password)

        # Spacer between buttons
        # spacerItem1 = QtWidgets.QSpacerItem(
        #     40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        # )
        # self.horizontalLayout_2.addItem(spacerItem1)

        # Enter button
        self.sign_in = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.sign_in.setObjectName("sign_in")
        self.horizontalLayout_2.addWidget(self.sign_in)

        # Title label
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 90, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")

        # Set central widget, menu bar, and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Retranslate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # conectar botões às funções correspondentes
        self.show_password.pressed.connect(self.show_password_pressed)
        self.show_password.released.connect(self.show_password_released)
        self.sign_in.clicked.connect(self.login)

        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.show_password)
        MainWindow.setTabOrder(self.show_password, self.sign_up)
        MainWindow.setTabOrder(self.sign_up, self.recover_password)
        MainWindow.setTabOrder(self.recover_password, self.sign_in)

    def show_password_pressed(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def show_password_released(self):
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)            

    def  login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == 'admin' and password == 'admin':
            print('Logging in...')
        else:
            print('Wrong credentials, try again.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Médico Modular"))
        self.label.setText(_translate("MainWindow", "Usuário"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.show_password.setText(_translate("MainWindow", "Show"))
        self.sign_up.setText(_translate("MainWindow", "Sign up"))
        self.recover_password.setText(_translate("MainWindow", 'Recover'))
        self.sign_in.setText(_translate("MainWindow", "Entrar"))
        self.label_3.setText(_translate("MainWindow", "Sistema Médico Modular"))


def main():
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #main_window = MainWindowController()
    #window = AddPatientController()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()