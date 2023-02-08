import tkinter as tk
import mysql.connector

# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='example')
cursor = cnx.cursor()

# Tkinter GUI for login
def login():
    def check_login():
        query = "SELECT * FROM users WHERE username='" + username_entry.get() + "' AND password='" + password_entry.get() + "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Login successful!")
        else:
            print("Login failed. Please try again.")

    window = tk.Tk()
    window.title("Login")
    window.geometry("300x150")

    username_label = tk.Label(text="Username:")
    username_label.grid(column=0, row=0)

    username_entry = tk.Entry()
    username_entry.grid(column=1, row=0)

    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=1)

    password_entry = tk.Entry(show="*")
    password_entry.grid(column=1, row=1)

    login_button = tk.Button(text="Login", command=check_login)
    login_button.grid(column=1, row=2)

    window.mainloop()

# Run the login GUI
login()

# Close the MySQL connection
cursor.close()
cnx.close()
