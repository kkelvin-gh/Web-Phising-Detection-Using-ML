from PyQt5 import QtCore, QtGui, QtWidgets
import feature_extractor

class Ui_Spam_detector(object):
    def setupUi(self, Spam_detector):
        Spam_detector.setObjectName("Spam_detector")
        Spam_detector.resize(600, 450)

        # Set window background color and centralize the window
        Spam_detector.setStyleSheet("background-color: #f0f0f0;")
        Spam_detector.setWindowIcon(QtGui.QIcon("icon.png"))
        Spam_detector.setWindowTitle("Spam Detector")

        self.centralwidget = QtWidgets.QWidget(Spam_detector)
        self.centralwidget.setObjectName("centralwidget")

        # URL Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #333;")

        # URL Input
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(120, 80, 420, 31))
        self.url_input.setObjectName("url_input")
        self.url_input.setStyleSheet("""
            background-color: white;
            border: 2px solid #cccccc;
            border-radius: 10px;
            padding: 5px;
            font-size: 12pt;
        """)

        # Check Button
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(240, 140, 120, 40))
        self.check_button.setObjectName("check_button")
        self.check_button.clicked.connect(self.button_click)
        self.check_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                font-size: 12pt;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Output Textbox
        self.output_text = QtWidgets.QTextEdit(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(50, 200, 500, 180))
        self.output_text.setObjectName("output_text")
        self.output_text.setStyleSheet("""
            background-color: white;
            border: 2px solid #cccccc;
            border-radius: 10px;
            padding: 10px;
            font-size: 11pt;
        """)

        # Title Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 400, 40))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font-size: 18pt; font-weight: bold; color: #333;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        Spam_detector.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Spam_detector)
        self.statusbar.setObjectName("statusbar")
        Spam_detector.setStatusBar(self.statusbar)

        self.retranslateUi(Spam_detector)
        QtCore.QMetaObject.connectSlotsByName(Spam_detector)

    def retranslateUi(self, Spam_detector):
        _translate = QtCore.QCoreApplication.translate
        Spam_detector.setWindowTitle(_translate("Spam_detector", "Phishing Detector"))
        self.check_button.setText(_translate("Spam_detector", "Check URL"))
        self.label.setText(_translate("Spam_detector", "URL:"))
        self.label_2.setText(_translate("Spam_detector", "Phishing Detector"))

    def button_click(self):
        text = self.url_input.text()
        obj = feature_extractor.feature_extractor(text)
        str1 = obj.extract()
        self.output_text.append(f"{str1}\n\n")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Spam_detector = QtWidgets.QMainWindow()
    ui = Ui_Spam_detector()
    ui.setupUi(Spam_detector)
    Spam_detector.show()
    sys.exit(app.exec_())
