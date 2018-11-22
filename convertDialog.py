from PyQt5 import uic
from PyQt5 import QtWidgets
import os

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'convertVN2000_DialogBase.ui'))


class ConvertVN2000Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(ConvertVN2000Dialog, self).__init__(parent)
        self.setupUi(self)
