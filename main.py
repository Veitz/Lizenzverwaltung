import sys
import csv
# from qtpy import QtWidgets, QmessageBox, QtGui
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QLabel

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Lizenzverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.readCsvFile("lizenzen.csv")
        self.ui.newEntryButton.clicked.connect(self.onNewEntry)
        self.ui.saveButton.clicked.connect(self.onSave)
        self.ui.deleteButton.clicked.connect(self.onDelete)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionInfo.triggered.connect(self.onInfo)


    def onDelete(self):
        if self.ui.lizenzTable.rowCount() > 0:
            self.ui.lizenzTable.removeRow(self.ui.lizenzTable.rowCount()-1)


    def onSave(self):
        with open('lizenzen.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"')

            rows = self.ui.lizenzTable.rowCount()
            for i in range(0, rows):
                rowContent = [
                    self.ui.lizenzTable.item(i, 0).text(),
                    self.ui.lizenzTable.item(i, 1).text(),
                    self.ui.lizenzTable.item(i, 2).text(),
                    self.ui.lizenzTable.item(i, 3).text()
                ]
                writer.writerow(rowContent)

    def onNewEntry(self):
        row = self.ui.lizenzTable.rowCount()
        self.ui.lizenzTable.insertRow(row)

        self.ui.lizenzTable.setItem(row, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.lizenzTable.setItem(row, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.lizenzTable.setItem(row, 2, QtWidgets.QTableWidgetItem(""))
        self.ui.lizenzTable.setItem(row, 3, QtWidgets.QTableWidgetItem(""))

        cell = self.ui.lizenzTable.item(row, 0)
        self.ui.lizenzTable.editItem(cell)

    def readCsvFile(self, filename):
        self.ui.lizenzTable.setRowCount(0)
        with open(filename, "r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.ui.lizenzTable.rowCount()
                self.ui.lizenzTable.insertRow(row)

                self.ui.lizenzTable.setItem(row, 0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.lizenzTable.setItem(row, 1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.lizenzTable.setItem(row, 2, QtWidgets.QTableWidgetItem(line[2]))
                self.ui.lizenzTable.setItem(row, 3, QtWidgets.QTableWidgetItem(line[3]))

    def onInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("InfoBox")
        msg.setText("Lizenzverwaltung - v0.1 \n "
                    " \n "
                    "Github: https://github.com/Veitz")
        #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.exec_()  # this will show our messagebox

        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

        # make a Hyperlink
        #linkTemplate = '<a href={0}>{1}</a>'
        #msg.setText(linkTemplate.format('https://github.com/Veitz', 'project on Github'))







window = MainWindow()

window.show()

sys.exit(app.exec_())
