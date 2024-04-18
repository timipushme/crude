from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import mysql.connector

def add_user_window():
    add_user_win =  Toplevel()
    add_user_win.title("Add User")

    Label(add_user_win, text="First Name:").pack()
    first_name_entry = Entry(add_user_win)
    first_name_entry.pack()

    Label(add_user_win, text="Last Name:").pack()
    last_name_entry = Entry(add_user_win)
    last_name_entry.pack()

    Label(add_user_win, text="Email:").pack()
    email_entry = Entry(add_user_win)
    email_entry.pack()

    def add_user():
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crude")
            cursor = conn.cursor()

            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users "
                "(id int auto_increment primary key, firstName TEXT, lastName TEXT, email TEXT)")


            insert_query = "INSERT INTO users (firstName, lastName, email) VALUES (%s, %s, %s)"
            user_data = (first_name_entry.get(), last_name_entry.get(), email_entry.get())
            cursor.execute(insert_query, user_data)
            conn.commit()

            messagebox.showinfo("Success", "User added successfuly!")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add user: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    add_button = Button(add_user_win, text="Add User", command= add_user)
    add_button.pack()




def delete_user_window():
    delete_user_win = Toplevel()
    delete_user_win.title("Delete User")

    Label(delete_user_win, text="User ID:").pack()
    user_id_entry = Entry(delete_user_win)
    user_id_entry()

    def delete_user_window():
        delete_user_win = Toplevel()
        delete_user_win.title("Delete User")

        # Create labels and entry widget for user ID
        Label(delete_user_win, text="User ID:").pack()
        user_id_entry = Entry(delete_user_win)
        user_id_entry.pack()

        # Connect to the database and delete the user
        def delete_user():
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="record")
                cursor = conn.cursor()

                # Delete user from the database
                delete_query = "DELETE FROM users WHERE id = %s"
                user_id = (user_id_entry.get(),)
                cursor.execute(delete_query, user_id)
                conn.commit()

                messagebox.showinfo("Success", "User deleted successfully!")

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to delete user: {e}")

            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

        # Create a button to delete the user
        delete_button = Button(delete_user_win, text="Delete User", command=delete_user)
        delete_button.pack()



    def delete_user():
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="crude")
            cursor = conn.cursor()

            delete_query = "DELETE FROM users WHERE id = %s"
            user_id = (user_id_entry.get())
            cursor.execute(delete_query,user_id)
            conn.commit()

            messagebox.showinfo("Success","User deleted successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error" f"Failed to delete user: {e}")




def main():
    root = Tk()
    root.title("User Management App")
    root.geometry("400x400")
    root.resizable(False, False)

    # Load and display the background image
    background_image = Image.open("background.jpeg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    #Create the rest of the UI on top of the background image
    btn_add_user = Button(root, text="Add User", width=10, command=add_user_window )
    btn_add_user.place(relx=0.1, rely=0.5)

    btn_update_user = Button(root, text="Update User", width=10, )
    btn_update_user.place(relx=0.3, rely=0.5)

    btn_delete_user = Button(root, text="Delete User", width=10, command=delete_user_window )
    btn_delete_user.place(relx=0.5, rely=0.5)

    btn_display_users = Button(root, text="Display Users", width=10, )
    btn_display_users.place(relx=0.7, rely=0.5)

    root.mainloop()

if __name__ == '__main__':
    main()