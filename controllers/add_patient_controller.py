from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from models.patient_model import Patient, session

class AddPatientController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Registrar paciente')
        self.setGeometry(100, 100, 400, 200)

        # Create form fields
        self.nome_label = QLabel('Nome', self)
        self.nome_input = QLineEdit(self)

        self.sobrenome_label = QLabel('Sobrenome', self)
        self.sobrenome_input = QLineEdit(self)

        self.pfj_label = QLabel('PFJ', self)
        self.pfj_input = QLineEdit(self)

        self.prontuario_label = QLabel('Prontuário', self)
        self.prontuario_input = QLineEdit(self)

        self.diagnostico_label = QLabel('Diagnóstico', self)
        self.diagnostico_input = QLineEdit(self)

        # Submit button
        self.gravar_button = QPushButton('Gravar', self)
        self.gravar_button.clicked.connect(self.add_patient)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.sobrenome_label)
        layout.addWidget(self.sobrenome_input)
        layout.addWidget(self.pfj_label)
        layout.addWidget(self.pfj_input)
        layout.addWidget(self.prontuario_label)
        layout.addWidget(self.prontuario_input)
        layout.addWidget(self.diagnostico_label)
        layout.addWidget(self.diagnostico_input)
        layout.addWidget(self.gravar_button)

        self.setLayout(layout)

    def add_patient(self):
        # Retrieve input data
        nome = self.nome_input.text()
        sobrenome = self.sobrenome_input.text()
        pfj = self.pfj_input.text()
        prontuario = self.prontuario_input.text()
        diagnostico = self.diagnostico_input.text()

        # Input validation
        if not nome or not sobrenome or not diagnostico or not pfj or not prontuario:
            QMessageBox.warning(self, 'Input Error', 'All fields are required!')
            return

        # Add patient to the database
        new_patient = Patient(nome=nome, sobrenome=sobrenome, pfj=pfj, prontuario=prontuario, diagnostico=diagnostico)
        session.add(new_patient)
        session.commit()

        # Show success message
        QMessageBox.information(self, 'Success', 'Patient added successfully!')

        # Clear inputs
        self.nome_input.clear()
        self.sobrenome_input.clear()
        self.pfj_input.clear()
        self.prontuario.clear()
        self.diagnostico_input.clear()
