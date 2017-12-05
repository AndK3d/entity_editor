import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog,QTableWidget,QTableWidgetItem, QHeaderView

import xml.etree.ElementTree as ET


qtCreatorFile = "entity.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QDialog, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.browse_folder_bt1.clicked.connect(self.browse_folder)

        self.initTable()

    def browse_folder(self):

        filename = QFileDialog.getOpenFileName(self, 'Open file','./', "XML files (*.xml)")

        if filename:
            self.CIGITaskConfig_path.setText(str(filename[0]))
            self.get_xml_entity_data(str(filename[0]))
            data = self.get_xml_entity_data(str(filename[0]))

            self.fill_table(data)


        return

    def initTable(self):

        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)

        hheader = self.tableWidget.horizontalHeader()

        hheader.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        hheader.setSectionResizeMode(1, QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.setHorizontalHeaderLabels(['Type', 'Name'])

    def get_xml_entity_data(self,xml_filename):

        xml_tree = ET.parse(xml_filename)
        entity_list = xml_tree.iter('Entity')

        return entity_list

    def fill_table(self,data):

        i = 0
        for row in data:
            self.tableWidget.setRowCount(i+1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.attrib['Type']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row.attrib['Name']))
            i = i + 1
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


