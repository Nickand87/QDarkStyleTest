from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QFormLayout, QListWidgetItem, QFrame
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp
import qdarktheme


class CustomerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Information")
        self.setGeometry(100, 100, 800, 500)  # Adjusted window size

        # Set style sheets
        darktheme_stylesheet = qdarktheme.load_stylesheet()

        # Central Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout(central_widget)

        # Font Settings
        font = QFont("Arial", 12)
        label_font = QFont("Arial", 10, QFont.Bold)

        # ID Frame
        id_frame = QFrame()
        id_frame.setFrameShape(QFrame.StyledPanel)
        id_layout = QHBoxLayout(id_frame)
        main_layout.addWidget(id_frame)

        # ID Field
        self.customer_id_entry = QLineEdit()
        self.customer_id_entry.setValidator(QIntValidator())
        self.customer_id_entry.setFont(font)
        id_label = QLabel("ID:")
        id_label.setFont(label_font)
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.customer_id_entry)

        # Horizontal Layout for Input Fields (Company Info and Contacts)
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)

        # Frame for Company Info
        company_info_frame = QFrame()
        company_info_frame.setFrameShape(QFrame.StyledPanel)
        company_info_layout = QFormLayout(company_info_frame)
        input_layout.addWidget(company_info_frame)

        # Company Info Title
        company_info_title = QLabel("Company Info")
        company_info_title.setFont(label_font)
        company_info_layout.addRow(company_info_title)

        # Company Info Fields
        self.customer_name_entry = QLineEdit()
        self.customer_address1_entry = QLineEdit()
        self.customer_address2_entry = QLineEdit()
        self.customer_phone_entry = QLineEdit()
        self.customer_emailfax_entry = QLineEdit()

        # Validators for Company Info Fields
        phone_reg_exp = QRegExp("[0-9\-]+")
        self.customer_phone_entry.setValidator(QRegExpValidator(phone_reg_exp))

        # Set Fonts and Add Widgets to Company Info Layout
        for label_text, widget in [
            ("Customer Name:", self.customer_name_entry),
            ("Address:", self.customer_address1_entry),
            ("Address:", self.customer_address2_entry),
            ("Phone #:", self.customer_phone_entry),
            ("Email/Fax:", self.customer_emailfax_entry)
        ]:
            label = QLabel(label_text)
            label.setFont(label_font)
            widget.setFont(font)
            company_info_layout.addRow(label, widget)

        # Frame for Contacts
        contacts_frame = QFrame()
        contacts_frame.setFrameShape(QFrame.StyledPanel)
        contacts_layout = QFormLayout(contacts_frame)
        input_layout.addWidget(contacts_frame)

        # Contacts Title
        contacts_title = QLabel("Contacts")
        contacts_title.setFont(label_font)
        contacts_layout.addRow(contacts_title)

        # Contact Fields
        self.contact_name_entry = QLineEdit()
        self.contact_address1_entry = QLineEdit()
        self.contact_address2_entry = QLineEdit()
        self.contact_phone_entry = QLineEdit()
        self.contact_emailfax_entry = QLineEdit()

        # Validators for Contact Fields
        self.contact_phone_entry.setValidator(QRegExpValidator(phone_reg_exp))

        # Set Fonts and Add Widgets to Contacts Layout
        for label_text, widget in [
            ("Contact Name:", self.contact_name_entry),
            ("Address:", self.contact_address1_entry),
            ("Address:", self.contact_address2_entry),
            ("Phone #:", self.contact_phone_entry),
            ("Email/Fax:", self.contact_emailfax_entry)
        ]:
            label = QLabel(label_text)
            label.setFont(label_font)
            widget.setFont(font)
            contacts_layout.addRow(label, widget)

        # Button Layout
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # Buttons
        self.submit_button = QPushButton("Submit")
        self.load_button = QPushButton("Load Customer")
        self.delete_button = QPushButton("Delete Customer")
        self.clear_button = QPushButton("Clear Fields")

        # Apply the custom font to buttons
        self.submit_button.setFont(font)
        self.load_button.setFont(font)
        self.delete_button.setFont(font)
        self.clear_button.setFont(font)

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_button)

        # List Widget for Customer Data
        self.customer_list = QListWidget()
        main_layout.addWidget(self.customer_list)
        self.customer_list.setStyleSheet("alternate-background-color: #505050;")
        self.customer_list.setAlternatingRowColors(True)

        # Set application-wide stylesheet using qdarktheme
        self.setStyleSheet(darktheme_stylesheet)

        # Test Data
        test_data = [
            "1 - John Doe - 123 Street",
            "2 - Jane Smith - 456 Avenue",
            "3 - Nick Jackson - 421 Cedarmont Dr."
        ]

        # Adding items to the list
        for item in test_data:
            QListWidgetItem(item, self.customer_list)

            self.submit_button.clicked.connect(self.on_submit_click)

        self.show()


    def on_submit_click(self):
        """Handle the submit button click event."""
        print("Hello World")

