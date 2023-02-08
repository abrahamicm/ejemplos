import tkinter as tk
import mysql.connector

# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='example')
cursor = cnx.cursor()

# Tkinter GUI for registration
def register():
    def create_user():
        query = "INSERT INTO users (username, password) VALUES ('" + username_entry.get() + "', '" + password_entry.get() + "')"
        cursor.execute(query)
        cnx.commit()
        print("User created successfully!")

    window = tk.Tk()
    window.title("Register")
    window.geometry("300x150")

    username_label = tk.Label(text="Username:")
    username_label.grid(column=0, row=0)

    username_entry = tk.Entry()
    username_entry.grid(column=1, row=0)

    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=1)

    password_entry = tk.Entry(show="*")
    password_entry.grid(column=1, row=1)

    register_button = tk.Button(text="Register", command=create_user)
    register_button.grid(column=1, row=2)

    window.mainloop()

# Run the registration GUI
register()

# Close the MySQL connection
cursor.close()
cnx.close()
