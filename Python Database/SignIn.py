# Sign In Page

from tkinter import *
from tkinter import messagebox
import pymysql


window = Tk()
window.title("SignIn Page")
window.geometry("600x250")

#### Driver Function

def click():
    entered_name = uname.get()
    entered_password = password.get()
    
    # Open database connection
    db = pymysql.connect("localhost","root","Saraswat@123","pythontest")
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO user(uname , password) VALUES ( '%s' , '%s')""" % (entered_name,entered_password)

    try:

   # Execute the SQL command
        cursor.execute(sql)
   # Commit your changes in the database
        db.commit()
        print('SignIn Successful')
        messagebox.showinfo("SignIn", "SignIn Successful")

    except:
   # Rollback in case there is any error
        db.rollback()
        messagebox.showinfo("SignIn", "SignIn UnSuccessful")

    # disconnect from server
    db.close()




####  UserName Label
Label (window , text = "\n USER NAME : ", font = "none 10 bold").grid(row=1, column=2,sticky= W)

####  Create a text Entry Box
uname = Entry(window, width=30)
uname.grid(row=1, column=3, sticky=W)

####  Password Label
Label (window , text = "\n PASSWORD : ", font = "none 10 bold").grid(row=2, column=2,sticky= W)

####  Create a text Entry Box
password = Entry(window, width=30)
password.grid(row=2, column=3, sticky=W)


#### Submit Button
Button(window, text="SUBMIT", width = 6, command= click).grid(row = 4, column =2, sticky = W)
Button(window, text='Quit', command=window.quit).grid(row=4, column=3, sticky=W)

#### run the main loop
window.mainloop()