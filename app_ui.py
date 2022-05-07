from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import uic
import sys

class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi('./app.ui', self)
        self.ui.show()
        self.showList()

    def showList(self):
        numbers = ['One','two']
        model = QStandardItemModel()

        for x in numbers:
            model.appendRow(QStandardItem(x))
        self.ui.listView.setModel(model)
app = QtWidgets.QApplication(sys.argv)
me = App()
# sys.exit(app.exec())
sys.exit(app.exec())