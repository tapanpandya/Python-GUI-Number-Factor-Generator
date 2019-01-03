from tkinter import *

def getFactor():
    #List for storing factors of entered number by the user
    factors = []
    lineno = 0
    # for clearing the listbox if it has any data inside it.
    listb.delete(0,END)
    #Defining global before variable to access and store values inside it to access it within program
    global value
    # StringVar for updating number
    global input

    value = int(user_input.get())
    input.set("Factors for {} are as follows".format(value))
    if value > 0:

        for i in range(1,value+1):
            if value%i==0:
                factors.append(i)
        for x in factors:
            v = factors[lineno]
            listb.insert(lineno+1, v)
            lineno = lineno + 1
        listb.pack()
    else:
        print("Something is not right!!!")

# Creating empty window and assigning window size in geometry
root = Tk()
root.geometry("300x370+100+100")
root.resizable(FALSE,FALSE)
listb = Listbox(root)

input = StringVar()
global value

l1 = Label(root, text="Factor Generator", font=("Courier", 16))
l1.pack()

note = Label(root, text="Note: Enter your desired number \n into the Entry box", font=("Courier", 8))
note.pack(fill=X, padx=15, pady=15)

user_input = Entry(root, bd=3, font=("Courier", 12))
user_input.pack(fill=X, pady=5, padx=10)

submit = Button(root, text="Get Factors", bg="light green", command=getFactor)
submit.pack(fill=X, pady=5, padx=10)

l = Label(root, textvariable=input)
l.pack()

# Adding scrollbar to our Listbox for batterment of user

scrollbar = Scrollbar(root, orient="vertical")
scrollbar.config(command=listb.yview)
scrollbar.pack(side="right", fill="y")

# Adding scrollbar to Listbox
listb.config(yscrollcommand=scrollbar.set)

root.mainloop()
