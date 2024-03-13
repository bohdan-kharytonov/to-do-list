import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_Widget
from database import database

class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dataBase = database()
        self.pushButton.clicked.connect(self.save_data)
        self.display_data_from_database()

    def save_data(self):
        if(len(self.lineEdit.text()) != 0):
            self.dataBase.input_data_to_database(self.lineEdit.text(), self.dateEdit.date().toString())
            self.listWidget.clear()
            self.lineEdit.clear()
            self.display_data_from_database()
        else:
            self.pop_up_empty_string()

    def display_data_from_database(self):
        for item in self.dataBase.get_data_from_database():
            item_str = " ".join(str(i).strip("(),") for i in item)
            list_item = QtWidgets.QListWidgetItem(item_str[1:])
            self.listWidget.addItem(list_item)
        pass
    def pop_up_empty_string(self):
        self.pop_up = QtWidgets.QLabel("Your string is empty")
        self.pop_up.setStyleSheet("background-color: red;")
        self.pop_up.resize(150, 100)
        self.pop_up.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
