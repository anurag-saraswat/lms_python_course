# My Glossarry Project
from tkinter import *


#### Functions
def click():
    print("abc")
    entered_text = textentry.get()   #collect data from text entry box
    output.delete(0.0 , END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = 'No Word In The Dictionary'
    output.insert(END , definition)
        	
#### main:
window = Tk()
window.title("My Computer Glossary")
window.configure(background = "white")

#### My Photo
photo1 = PhotoImage(file="image1.gif")
Label(window, image=photo1, bg = "white").grid(row = 0,column=0,sticky=W)

#### Create Label
Label (window , text = "\nEnter the word you would like a defination for: ", bg = "white" , font = "none 12 bold").grid(row=1, column=0,sticky= W)

####  Create a text Entry Box
textentry = Entry(window, width=30)
textentry.grid(row=2, column=0, sticky=W)

#### Add Submit Button
Button(window, text="SUBMIT", width = 6, command= click).grid(row = 3, column =0, sticky = W)

#### Add Another Label
Label (window, text = "\nDefination : ", font = "none 18 bold" ,bg="white").grid(row=4, column=0,sticky= W)

#### Create a text box
output = Text(window, width=75, height=6, wrap = WORD, background = "white")
output.grid(row=5, column=0, columnspan=2, stick=W)

#### The Dictionary
my_compdictionary = {
	'algorithm':'a process or set of rules to be followed in calculations or other problem-solving operations','program':'structured collection of instruction sequences that perform a specific task when executed by a computer','bug':'A software bug is an error, flaw, failure or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways.'
}


Button(window, text='Quit', command=window.quit).grid(row=3, column=1, sticky=W)


#### run the main loop
window.mainloop()
