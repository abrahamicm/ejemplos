import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton
import pymysql

class CreateUser(QDialog):
    def __init__(self):
        super().__init__()
        
        self.label_username = QLabel("Username:", self)
        self.line_edit_username = QLineEdit(self)
        self.label_password = QLabel("Password:", self)
        self.line_edit_password = QLineEdit(self)
        self.button_create = QPushButton("Create", self)
        self.button_create.clicked.connect(self.create_user)
        
        self.label_username.move(20, 20)
        self.line_edit_username.move(80, 20)
        self.label_password.move(20, 60)
        self.line_edit_password.move(80, 60)
        self.button_create.move(20, 100)
        
        self.setWindowTitle("Create User")
        self.setGeometry(300, 300, 300, 150)
        
    def create_user(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()
        
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='example'
        )
        
        try:
            with connection.cursor() as cursor:
                # Insert the user into the database
                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
                
            # Commit the transaction
            connection.commit()
            
            self.line_edit_username.setText("")
            self.line_edit_password.setText("")
            
        finally:
            connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_user = CreateUser()
    create_user.show()
    sys.exit(app.exec_())
