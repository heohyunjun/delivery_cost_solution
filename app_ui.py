from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import uic
import sys

class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None, food=None):
        super().__init__(parent)
        self.ui = uic.loadUi('./app.ui', self)
        self.ui.show()

        self.food = food
        self.showList()

    def showList(self):
        # numbers = ['One','two']
        model = QStandardItemModel()
        # model.appendRow(self.food)
        for x in self.food:
            model.appendRow(QStandardItem(x))
        self.ui.listView.setModel(model)

    def order_confirm_buttion(self):
        pass

    def order_reject_buttion(self):
        pass

    def call_rider_buttion(self):
        pass

    def cancel_rider_button(self):
        pass
# app = QtWidgets.QApplication(sys.argv)
# me = App()
# # sys.exit(app.exec())
# sys.exit(app.exec())