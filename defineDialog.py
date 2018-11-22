from PyQt5 import uic
from PyQt5 import QtWidgets
import os

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'define_dialog.ui'))


class DefineDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(DefineDialog, self).__init__(parent)
        self.setupUi(self)
 
