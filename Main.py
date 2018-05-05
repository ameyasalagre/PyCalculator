# Main Controller
# Created Date 5/5/218
# Author:- Ameya Salagre

import sys
from PyQt5.QtWidgets import QApplication
from My_Model import mycalculator

app = QApplication(sys.argv)

calculator = mycalculator()

sys.exit(app.exec_())
