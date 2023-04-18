# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 494)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lizenzTable = QtWidgets.QTableWidget(self.centralWidget)
        self.lizenzTable.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.lizenzTable.setGridStyle(QtCore.Qt.SolidLine)
        self.lizenzTable.setObjectName("lizenzTable")
        self.lizenzTable.setColumnCount(4)
        self.lizenzTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lizenzTable.setItem(1, 3, item)
        self.lizenzTable.horizontalHeader().setVisible(True)
        self.lizenzTable.horizontalHeader().setDefaultSectionSize(110)
        self.lizenzTable.horizontalHeader().setStretchLastSection(True)
        self.lizenzTable.verticalHeader().setVisible(False)
        self.lizenzTable.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.lizenzTable, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newEntryButton = QtWidgets.QPushButton(self.centralWidget)
        self.newEntryButton.setObjectName("newEntryButton")
        self.horizontalLayout_2.addWidget(self.newEntryButton)
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 530, 31))
        self.menuBar.setObjectName("menuBar")
        self.menuMen = QtWidgets.QMenu(self.menuBar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.actionExit)
        self.menuBar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lizenzTable.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Dies ist ein kleines Tool zum Verwalten von Lizenz-Keys</p></body></html>"))
        item = self.lizenzTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.lizenzTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.lizenzTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LizenzName"))
        item = self.lizenzTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AblaufDatum"))
        item = self.lizenzTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LizenzSchlüssel"))
        item = self.lizenzTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bemerkung"))
        __sortingEnabled = self.lizenzTable.isSortingEnabled()
        self.lizenzTable.setSortingEnabled(False)
        item = self.lizenzTable.item(0, 0)
        item.setText(_translate("MainWindow", "Windows Lizenz"))
        item = self.lizenzTable.item(0, 1)
        item.setText(_translate("MainWindow", "28.04.2023"))
        item = self.lizenzTable.item(0, 2)
        item.setText(_translate("MainWindow", "dfg-dfg-arw-234-dgdf-h54whtr"))
        item = self.lizenzTable.item(0, 3)
        item.setText(_translate("MainWindow", "nur ein Placeholder"))
        item = self.lizenzTable.item(1, 0)
        item.setText(_translate("MainWindow", "Backup"))
        item = self.lizenzTable.item(1, 1)
        item.setText(_translate("MainWindow", "01.01.1970"))
        item = self.lizenzTable.item(1, 2)
        item.setText(_translate("MainWindow", "456546-dsgdsf-13ref-34tge"))
        item = self.lizenzTable.item(1, 3)
        item.setText(_translate("MainWindow", "xXx"))
        self.lizenzTable.setSortingEnabled(__sortingEnabled)
        self.newEntryButton.setText(_translate("MainWindow", "Neuen Eintrag"))
        self.saveButton.setText(_translate("MainWindow", "Speichern"))
        self.deleteButton.setText(_translate("MainWindow", "Eintrag Löschen"))
        self.menuMen.setTitle(_translate("MainWindow", "Menü"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))