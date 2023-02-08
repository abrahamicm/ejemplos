import tkinter as tk
import mysql.connector
# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='example')
cursor = cnx.cursor()

# Tkinter GUI for CRUD
def crud():
    def read_users():
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        result_label.config(text=result)

    def create_user():
        query = "INSERT INTO users (username, password) VALUES ('" + username_entry.get() + "', '" + password_entry.get() + "')"
        cursor.execute(query)
        cnx.commit()
        print("User created successfully!")

    def update_user():
        query = "UPDATE users SET password='" + password_entry.get() + "' WHERE username='" + username_entry.get() + "'"
        cursor.execute(query)
        cnx.commit()
        print("User updated successfully!")

    def delete_user():
        query = "DELETE FROM users WHERE username='" + username_entry.get() + "'"
        cursor.execute(query)
        cnx.commit()
        print("User deleted successfully!")

    window = tk.Tk()
    window.title("CRUD")
    window.geometry("300x300")

    username_label = tk.Label(text="Username:")
    username_label.grid(column=0, row=0)

    username_entry = tk.Entry()
    username_entry.grid(column=1, row=0)

    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=1)

    password_entry = tk.Entry(show="*")
    password_entry.grid(column=1, row=1)

    read_button = tk.Button(text="Read", command=read_users)
    read_button.grid(column=0, row=2)

    create_button = tk.Button(text="Create", command=create_user)
    create_button.grid(column=1, row=2)

    update_button = tk.Button(text="Update", command=update_user)
    update_button.grid(column=0, row=3)

    delete_button = tk.Button(text="Delete", command=delete_user)
    delete_button.grid(column=1, row=3)

    result_label = tk.Label(text="")
    result_label.grid(column=0, row=4, columnspan=2)

    window.mainloop()

# Run the CRUD GUI
crud()

# Close the MySQL connection
cursor.close()
cnx.close()