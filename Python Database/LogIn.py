# Login Page

from tkinter import *
import pymysql
from tkinter import messagebox


window = Tk()
window.title("Log In")
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
    sql = """SELECT * FROM user where uname = '%s'""" % (entered_name)

    try:

        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        var = results[0][1]
        if(var == entered_password):
            messagebox.showinfo("LogIn", "LogIn Successful")
        else:
            messagebox.showinfo("LogIn", "LogIn UnSuccessful")

    except:
        print ("Error: unable to fetch data")




####  UserName Label
Label (window , text = "\nENTER USER NAME : ", font = "none 10 bold").grid(row=1, column=2,sticky= W)

####  Create a text Entry Box
uname = Entry(window, width=30)
uname.grid(row=1, column=3, sticky=W)

####  Password Label
Label (window , text = "\n ENTER PASSWORD : ", font = "none 10 bold").grid(row=2, column=2,sticky= W)

####  Create a text Entry Box
password = Entry(window, width=30)
password.grid(row=2, column=3, sticky=W)


#### Submit Button
Button(window, text="SUBMIT", width = 6, command= click).grid(row = 4, column =2, sticky = W)
Button(window, text='Quit', command=window.quit).grid(row=4, column=3, sticky=W)

#### run the main loop
window.mainloop()
