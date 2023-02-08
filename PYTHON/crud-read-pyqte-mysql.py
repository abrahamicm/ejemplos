import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QPushButton
import pymysql

class ReadUser(QDialog):
    def __init__(self):
        super().__init__()
        
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Username", "Password"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.setEditTriggers(self.table_widget.NoEditTriggers)
        
        self.button_refresh = QPushButton("Refresh", self)
        self.button_refresh.clicked.connect(self.load_data)
        
        self.table_widget.move(20, 20)
        self.button_refresh.move(20, 260)
        
        self.setWindowTitle("Read User")
        self.setGeometry(300, 300, 400, 300)
        
        self.load_data()
        
    def load_data(self):
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='example'
        )
        
        try:
            with connection.cursor() as cursor:
                # Select all users from the database
                sql = "SELECT * FROM users"
                cursor.execute(sql)
                
                result = cursor.fetchall()
                
                self.table_widget.setRowCount(0)
                for row_index, row_data in enumerate(result):
                    self.table_widget.insertRow(row_index)
                    for column_index, data in enumerate(row_data):
                        self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        
        finally:
            connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    read_user = ReadUser()
    read_user.show()
    sys.exit(app.exec_())
