# My Glossarry Project
from tkinter import *
from tkinter import messagebox
import pymysql


#### Functions For fetching word from database
def getWord():
    entered_text = textentry.get()   #collect data from text entry box
    output.delete(0.0 , END)
    # Open database connection
    db = pymysql.connect("localhost","root","Saraswat@123","pythontest")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = """SELECT * FROM dictionary where word = '%s'""" % (entered_text)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        var = results[0][1]
    except:
        var = 'No Word In The Dictionary'
    output.insert(END , var)


#### Function For Addition Of word to database
def addWord():
    entered_word = dictword.get()
    entered_defination = dict_defination.get()
    # Open database connection
    db = pymysql.connect("localhost","root","Saraswat@123","pythontest")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO dictionary(word , defination) VALUES ( '%s' , '%s')""" % (entered_word,entered_defination)
    try:
    # Execute the SQL command
        cursor.execute(sql)
    # Commit your changes in the database
        db.commit()
        print('Word Added Successful')
        messagebox.showinfo("Dictionary", "Word Is Successfully Added To Dictionary")

    except:
    # Rollback in case there is any error
        db.rollback()
        messagebox.showinfo("Dictionary", "Word Is Not Added To Dictionary Try Again")

    # disconnect from server
    db.close()
     






#### main:
window = Tk()
window.title("My Computer Glossary")
window.configure(background = "white")
window.geometry("1000x1000")
#### My Photo
photo1 = PhotoImage(file="image1.gif")
Label(window, image=photo1, bg = "white").grid(row = 0,column=0,sticky=W)







##### CODE FOR GETTING WORD
#### Create Label
Label (window , text = "\nEnter the word you would like a defination for:\n", bg = "white" , font = "none 18 bold").grid(row=1, column=0,sticky= W)

####  Create a text Entry Box
textentry = Entry(window, width=30)
textentry.grid(row=2, column=0, sticky=W)

#### Add Submit Button
Button(window, text="SUBMIT", width = 6, command= getWord).grid(row = 3, column =0, sticky = W)

#### Add Button
Button(window, text='Quit', command=window.quit).grid(row=3, column=1, sticky=W)

#### Add Another Label
Label (window, text = "\nDefination : ", font = "none 18 bold" ,bg="white").grid(row=4, column=0,sticky= W)

#### Create a text box
output = Text(window, width=75, height=6, wrap = WORD, background = "white")
output.grid(row=5, column=0, columnspan=2, stick=W)


#### code for Addition in Dictionary

Label (window , text = "\nWant To Add in Dictionary: \n", bg = "white" , font = "none 20 bold").grid(row=7, column=0,sticky= W)
Label (window , text = "Word", bg = "white" , font = "none 20 bold").grid(row=8, column=0,sticky= W)
dictword = Entry(window, width=30)
dictword.grid(row=9, column=0, sticky=W)

Label (window , text = "Defination", bg = "white" , font = "none 20 bold").grid(row=8, column=1,sticky= W)
dict_defination = Entry(window, width=30)
dict_defination.grid(row=9, column=1, sticky=W)

Button(window, text="ADD WORD", width = 6, command= addWord).grid(row = 10, column =0, sticky = W)



#### run the main loop
window.mainloop()
