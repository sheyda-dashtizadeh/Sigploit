import sys
import os
import signal
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import qdarkstyle
from subprocess import check_call
from attack_forms import SRIForm, SRISMForm, ATIForm, ULForm, IMSIForm, MTSMSForm, PurgeForm, PSIForm, CLForm


purge_path = os.path.join(os.getcwd(), 'ss7/attacks/dos/prgms')
simsi_path = os.path.join(os.getcwd(), 'ss7/attacks/fraud/simsi')
mtsms_path = os.path.join(os.getcwd(), 'ss7/attacks/fraud/mtsms')
cl_path = os.path.join(os.getcwd(), 'ss7/attacks/fraud/cl')
ul_path = os.path.join(os.getcwd(), 'ss7/attacks/interception/ul')
sri_path = os.path.join(os.getcwd(), 'ss7/attacks/tracking/sri')
srism_path = os.path.join(os.getcwd(), 'ss7/attacks/tracking/srism')
psi_path = os.path.join(os.getcwd(), 'ss7/attacks/tracking/psi')
ati_path = os.path.join(os.getcwd(), 'ss7/attacks/tracking/ati')
srigprs_path = os.path.join(os.getcwd(), 'ss7/attacks/tracking/srigprs')


class LocationTrackingMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Location Tracking')
        self.setGeometry(200, 200, 800, 500)

        self.label = QLabel('Location Tracking', self)
        self.label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #007bff")
        self.label.setAlignment(Qt.AlignCenter)
        self.category_label = QLabel(
            'Select a Message from the list below', self)
        self.category_label.setStyleSheet("font-size: 16px; font-weight: bold")
        self.category_label.setAlignment(Qt.AlignCenter)

        self.messages_list = [
            {'message': 'SendRoutingInfo', 'category': 'CAT1'},
            {'message': 'ProvideSubscriberInfo', 'category': 'CAT2'},
            {'message': 'SendRoutingInfoForSM', 'category': 'CAT3'},
            {'message': 'AnyTimeInterrogation', 'category': 'CAT4'},
        ]

        self.list_widget = QListWidget(self)

        for item in self.messages_list:
            button = QPushButton(item['message'])
            button.setMinimumHeight(50)
            item_widget = QWidget()
            layout = QHBoxLayout()
            layout.addWidget(button)
            item_widget.setLayout(layout)
            list_item = QListWidgetItem()
            list_item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, item_widget)
            button.clicked.connect(
                lambda _, item=item: self.handle_choice(item))

        self.back_button = QPushButton('Back to Attacks Menu', self)
        self.back_button.clicked.connect(self.back_to_attacks_menu)
        self.back_button.setMinimumHeight(50)

        # Layout managers
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.label)
        button_layout.addWidget(self.category_label)
        button_layout.addWidget(self.list_widget)
        button_layout.addWidget(self.back_button)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def handle_choice(self, idx):
        choice = idx['message']
        if choice == 'SendRoutingInfo':
            self.run_sri_attack()
        elif choice == 'ProvideSubscriberInfo':
            self.run_psi_attack()
        elif choice == 'SendRoutingInfoForSM':
            self.run_srism_attack()
        elif choice == 'AnyTimeInterrogation':
            self.run_ati_attack()
        elif choice == 'SendRoutingInfoForGPRS':
            self.run_srigprs_attack()

    def run_sri_attack(self):
        self.SRIForm = SRIForm()
        self.SRIForm.show()

    def run_psi_attack(self):
        self.psiForm = PSIForm()
        self.psiForm.show()

    def run_srism_attack(self):
        self.SRISMForm = SRISMForm()
        self.SRISMForm.show()

    def run_ati_attack(self):
        self.ATIForm = ATIForm()
        self.ATIForm.show()

    def run_srigprs_attack(self):
        jar_file = 'SendRoutingInfoForGPRS.jar'
        try:
            srigprs = check_call(
                ['java', '-jar', os.path.join(srigprs_path, jar_file)])
            if srigprs == 0:
                QMessageBox.information(self, 'SendRoutingInfoForGPRS Attack',
                                        'SendRoutingInfoForGPRS Attack executed successfully.')
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"SendRoutingInfoForGPRS Failed to Launch: {str(e)}")

    def back_to_attacks_menu(self):
        self.close()


class InterceptionMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Interception')
        self.setGeometry(200, 200, 800, 400)

        self.form_layout = QFormLayout()

        self.label = QLabel('Interception', self)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold")
        self.label.setAlignment(Qt.AlignCenter)
        self.form_layout.addWidget(self.label)

        self.category_label = QLabel('Select a Message from the below', self)
        self.category_label.setStyleSheet("font-size: 16px; font-weight: bold")
        self.category_label.setAlignment(Qt.AlignCenter)
        self.form_layout.addWidget(self.category_label)

        self.messages_list = [
            {'message': 'UpdateLocation-SMS Interception', 'category': 'CAT3'},
        ]

        self.buttons = []
        for idx, item in enumerate(self.messages_list):
            button = QPushButton(item['message'], self)
            button.setGeometry(200, 160 + idx * 40, 500, 30)
            button.setMinimumHeight(50)
            button.clicked.connect(lambda _, idx=idx: self.handle_choice(idx))
            self.form_layout.addWidget(button)
            self.buttons.append(button)

        self.back_button = QPushButton('Back to Attacks Menu', self)
        self.back_button.clicked.connect(self.back_to_attacks_menu)
        self.back_button.setMinimumHeight(50)
        self.form_layout.addWidget(self.back_button)
        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        self.setLayout(layout)

    def handle_choice(self, idx):
        if 0 <= idx < len(self.messages_list):
            choice = self.messages_list[idx]['message']
            if choice == 'UpdateLocation-SMS Interception':
                self.ul()

    def ul(self):
        self.ULForm = ULForm()
        self.ULForm.show()

    def back_to_attacks_menu(self):
        self.close()


class FraudMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Fraud')
        self.setGeometry(200, 200, 800, 400)

        self.form_layout = QVBoxLayout()

        self.label = QLabel('Fraud', self)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold")
        self.label.setGeometry(380, 30, 300, 30)
        self.label.setAlignment(Qt.AlignCenter)

        self.category_label = QLabel('Select a Message from the below', self)
        self.category_label.setStyleSheet("font-size: 16px; font-weight: bold")
        self.category_label.setGeometry(250, 80, 400, 30)
        self.category_label.setAlignment(Qt.AlignCenter)

        self.messages_label = QLabel(
            'Message'.rjust(10) + '\t\t\t\tCategory', self)
        self.messages_label.setStyleSheet("font-size: 14px; font-weight: bold")
        self.messages_label.setGeometry(180, 120, 500, 30)
        self.messages_label.setAlignment(Qt.AlignCenter)

        self.form_layout.addWidget(self.label)
        self.form_layout.addWidget(self.category_label)
        self.form_layout.addWidget(self.messages_label)

        self.messages_list = [
            {'message': 'SendIMSI', 'category': 'CAT3'},
            {'message': 'MTForwardSMS SMS Spoofing', 'category': 'CAT3'},
            {'message': 'CancelLocation', 'category': 'CAT3'},
        ]

        self.buttons = []
        for idx, item in enumerate(self.messages_list):
            button = QPushButton(item['message'], self)
            button.setGeometry(200, 160 + idx * 40, 500, 30)
            button.clicked.connect(lambda _, idx=idx: self.handle_choice(idx))
            button.setMinimumHeight(50)
            self.form_layout.addWidget(button)
            self.buttons.append(button)

        self.back_button = QPushButton('Back to Attacks Menu', self)
        self.back_button.clicked.connect(self.back_to_attacks_menu)
        self.back_button.setMinimumHeight(50)

        self.form_layout.addWidget(self.back_button)

        self.setLayout(self.form_layout)

    def handle_choice(self, idx):
        if 0 <= idx < len(self.messages_list):
            choice = self.messages_list[idx]['message']
            if choice == 'SendIMSI':
                self.simsi()
            elif choice == 'MTForwardSMS SMS Spoofing':
                self.mtsms()
            elif choice == 'CancelLocation':
                self.CLForm = CLForm()
                self.CLForm.show()

    def simsi(self):
        self.imsiForm = IMSIForm()
        self.imsiForm.show()

    def mtsms(self):
        self.mtsmsForm = MTSMSForm()
        self.mtsmsForm.show()

    def back_to_attacks_menu(self):
        self.close()


class DoSMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Denial of Service')
        self.setGeometry(200, 200, 800, 400)

        self.v_layout = QVBoxLayout()

        self.label = QLabel('Denial of Service', self)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumHeight(50)
        self.v_layout.addWidget(self.label)

        self.category_label = QLabel('Select a Message from the below', self)
        self.category_label.setStyleSheet("font-size: 16px; font-weight: bold")
        self.category_label.setAlignment(Qt.AlignCenter)
        self.category_label.setMinimumHeight(50)
        self.v_layout.addWidget(self.category_label)

        self.messages_label = QLabel(
            'Message', self)
        self.messages_label.setStyleSheet("font-size: 14px; font-weight: bold")
        self.messages_label.setAlignment(Qt.AlignCenter)
        self.messages_label.setMinimumHeight(50)
        self.v_layout.addWidget(self.messages_label)

        self.messages_list = [
            {'message': 'PurgeMS-Subscriber DoS', 'category': 'CAT3'},
        ]

        self.buttons = []
        for idx, item in enumerate(self.messages_list):
            button = QPushButton(item['message'], self)
            self.v_layout.addWidget(button)
            button.clicked.connect(lambda _, idx=idx: self.handle_choice(idx))
            button.setMinimumHeight(50)
            self.buttons.append(button)

        self.back_button = QPushButton('Back to Attacks Menu', self)
        self.back_button.clicked.connect(self.back_to_attacks_menu)
        self.back_button.setMinimumHeight(50)
        self.v_layout.addWidget(self.back_button)

        self.setLayout(self.v_layout)

    def handle_choice(self, idx):
        if 0 <= idx < len(self.messages_list):
            choice = self.messages_list[idx]['message']
            if choice == 'PurgeMS-Subscriber DoS':
                self.run_dos_attack()

    def run_dos_attack(self):
        self.Purge = PurgeForm()
        self.Purge.show()

    def back_to_attacks_menu(self):
        self.close()


class AttacksMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Attacks Menu')
        self.setGeometry(200, 200, 800, 400)

        self.v_layout = QVBoxLayout()

        self.label = QLabel('Choose From the Below Attack Categories', self)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumHeight(65)
        self.v_layout.addWidget(self.label)

        self.location_tracking_button = QPushButton(
            'Location Tracking', self)
        self.location_tracking_button.clicked.connect(
            self.open_location_tracking)
        self.location_tracking_button.setGeometry(250, 100, 300, 30)
        self.location_tracking_button.setMinimumHeight(50)
        self.v_layout.addWidget(self.location_tracking_button)

        self.interception_button = QPushButton(
            'Call and SMS Interception', self)
        self.interception_button.clicked.connect(self.open_interception)
        self.interception_button.setGeometry(250, 150, 300, 30)
        self.interception_button.setMinimumHeight(50)
        self.v_layout.addWidget(self.interception_button)

        self.fraud_button = QPushButton('Fraud', self)
        self.fraud_button.clicked.connect(self.open_fraud)
        self.fraud_button.setGeometry(250, 200, 300, 30)
        self.fraud_button.setMinimumHeight(50)
        self.v_layout.addWidget(self.fraud_button)

        self.dos_button = QPushButton('Denial of Service(DoS)', self)
        self.dos_button.clicked.connect(self.open_dos)
        self.dos_button.setGeometry(250, 250, 300, 30)
        self.dos_button.setMinimumHeight(50)
        self.v_layout.addWidget(self.dos_button)

        self.back_button = QPushButton('Back to Main Menu', self)
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.back_button.setGeometry(250, 350, 300, 30)
        self.back_button.setMinimumHeight(35)
        self.v_layout.addWidget(self.back_button)

        self.setLayout(self.v_layout)

    def open_location_tracking(self):
        self.location_tracking_menu = LocationTrackingMenu()
        self.location_tracking_menu.show()

    def open_interception(self):
        self.interception_menu = InterceptionMenu()
        self.interception_menu.show()

    def open_fraud(self):
        self.fraud_menu = FraudMenu()
        self.fraud_menu.show()

    def open_dos(self):
        self.dos_menu = DoSMenu()
        self.dos_menu.show()

    def back_to_main_menu(self):
        self.close()


class SiGploitMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SiGploit - Signaling Exploitation Framework')
        self.setGeometry(100, 100, 800, 600)

        self.v_layout = QVBoxLayout()
        self.label = QLabel(
            'Signaling Exploitation Framework (GUI Version)', self)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold")
        self.label.setMinimumSize(600, 60)
        self.label.setAlignment(Qt.AlignCenter)
        self.version_label = QLabel('Version: BETA 1.0', self)
        self.version_label.setStyleSheet("font-size: 16px; color: #777777")
        self.version_label.setMinimumSize(200, 30)
        self.version_label.setAlignment(Qt.AlignCenter)
        self.author_label = QLabel('Author: Loay AbdelRazek (@sigploit)', self)
        self.author_label.setStyleSheet("font-size: 16px; color: #777777")
        self.author_label.setMinimumSize(200, 30)
        self.author_label.setAlignment(Qt.AlignCenter)
        self.contributors_label = QLabel('Contributors:', self)
        self.contributors_label.setStyleSheet(
            "font-size: 16px; font-weight: bold")
        self.contributors_label.setMinimumSize(200, 30)
        self.contributors_label.setAlignment(Qt.AlignCenter)

        self.contributors_list = [
            'Rosalia D\'Alessandro - TelecomItalia',
            'Sheyda Dashtizadeh - Sheyda-dashtizadeh',
        ]

        self.contributors = QLabel(self)
        self.contributors.setText('\n'.join(self.contributors_list))
        self.contributors.setStyleSheet("font-size: 14px; color: #333333")
        self.contributors.setMinimumSize(400, 90)

        self.ss7_button = QPushButton(
            'SS7 - 2G/3G Voice and SMS attacks', self)
        self.ss7_button.clicked.connect(self.open_ss7_attacks)
        self.ss7_button.setMinimumSize(300, 30)

        self.diameter_button = QPushButton(
            'Diameter - 4G Data attacks (Coming Soon)', self)
        self.diameter_button.clicked.connect(self.show_coming_soon_message)
        self.diameter_button.setMinimumSize(300, 30)

        self.gtp_button = QPushButton(
            'GTP - 3G Data attacks (Coming Soon)', self)
        self.gtp_button.clicked.connect(self.show_coming_soon_message)
        self.gtp_button.setMinimumSize(300, 30)

        self.sip_button = QPushButton(
            'SIP - 4G VoLTE attacks (Coming Soon)', self)
        self.sip_button.clicked.connect(self.show_coming_soon_message)
        self.sip_button.setMinimumSize(300, 30)

        self.quit_button = QPushButton('Quit SiGploit', self)
        self.quit_button.clicked.connect(self.quit_app)
        self.quit_button.setMinimumSize(300, 30)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.label)
        widget_layout.addWidget(self.version_label)
        widget_layout.addWidget(self.author_label)
        widget_layout.addWidget(self.contributors_label)
        widget_layout.addWidget(self.contributors)
        widget_layout.addWidget(self.ss7_button)
        widget_layout.addWidget(self.diameter_button)
        widget_layout.addWidget(self.gtp_button)
        widget_layout.addWidget(self.sip_button)
        widget_layout.addWidget(self.quit_button)

        self.setLayout(widget_layout)

    def open_ss7_attacks(self):
        self.attacks_menu = AttacksMenu()
        self.attacks_menu.show()

    def show_coming_soon_message(self):
        message_box = QMessageBox(self)
        message_box.setText('This feature is coming soon in future versions.')
        message_box.setWindowTitle('Coming Soon')
        message_box.setIcon(QMessageBox.Information)
        message_box.exec_()

    def quit_app(self):
        self.close()

    def signal_handler(self, signal, frame):
        print('\nYou are now exiting SiGploit...')
        time.sleep(1)
        sys.exit(0)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit SiGploit', 'Are you sure you want to quit SiGploit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    menu = SiGploitMenu()
    menu.show()
    sys.exit(app.exec_())
