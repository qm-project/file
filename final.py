from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1080x1080")
def hide_me(event):
    pressed.eingabefeld.pack_forget()

def selected(event):

    if clicked.get() == 'Keine Angabe':
        myLabel = Label(root, fg='#e63946', text="Hey, " + eingabefeld_wert.get() + "we accept that you do not want to provide information about your situation, but for the best experience we highly recommend it.").pack()

    else:
        myLabel = Label(root, fg='medium sea green', text="Hey, " + eingabefeld_wert.get() + "Start tracking your expenses by clicking on submit!").pack()


Abschluss =  [
   "Please select",
    "Student",
    "employee",
"Master",
    "Keine Angabe",
]



Label(root, text="Name").pack()


eingabefeld_wert= StringVar()
eingabefeld= Entry(root, textvariable=eingabefeld_wert)
eingabefeld.pack()


Label(root, text="EMail").pack()

eingabefeld_wert2= StringVar()
eingabefeld2= Entry(root, textvariable=eingabefeld_wert2)
eingabefeld2.pack()


Label(root, text="Nationality").pack()

eingabefeld_wert3= StringVar()
eingabefeld3= Entry(root, textvariable=eingabefeld_wert3)
eingabefeld3.pack()

clicked = StringVar()
clicked.set(Abschluss[0])

drop1 = OptionMenu(root, clicked, *Abschluss, command=selected)
drop1.pack(pady=20)


def pressed():


    # add some style
    style = ttk.Style()
    # pick a theme

    # configure our treeview colors
    # clam/ default/ alt/ = ändert oberste reihe
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=35,  # each row in treeview-> how fat or skinny
                    fieldbackground="white"
                    )
    # change selected color (wenn man drauf clickt die farbe)
    style.map('Treeview',
              background=[('selected', 'green')])

    my_tree = ttk.Treeview(root)

    # Columns
    my_tree['columns'] = ("Product name", "Category", "Date")
    my_tree.column("#0", width=120, minwidth=30)
    my_tree.column("Product name", anchor=W, width=140)
    my_tree.column("Category", anchor=CENTER, width=100)
    my_tree.column("Date", anchor=W, width=140)

    # Headings
    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("Product name", text="Product name", anchor=W)
    my_tree.heading("Category", text="Category", anchor=CENTER)
    my_tree.heading("Date", text="Date", anchor=W)

    data = [
        ["Macbook Air", "Electronics", "21.06"],
        ["Macbook Pro", "Electronics", "21.06"],
        ["Acer Swift 3", "Electronics", "21.06"]
    ]
    global count
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text="parent", values=(record[0], record[1], record[2]))
        count += 1

    my_tree.pack(pady=20)

    add_frame = Frame(root)
    add_frame.pack(pady=20)

    pl = Label(add_frame, text="Product name")
    pl.grid(row=0, column=0)

    cl = Label(add_frame, text="Category")
    cl.grid(row=0, column=1)

    dl = Label(add_frame, text="Date")
    dl.grid(row=0, column=2)

    product_box = Entry(add_frame)
    product_box.grid(row=1, column=0)

    category_box = Entry(add_frame)
    category_box.grid(row=1, column=1)

    date_box = Entry(add_frame)
    date_box.grid(row=1, column=2)

    # Add an expense
    def add_expenses():
        global count
        my_tree.insert(parent='', index='end', iid=count, text="parent",
                       values=(product_box.get(), category_box.get(), date_box.get()))
        count += 1

        product_box.delete(0, END)
        category_box.delete(0, END)
        date_box.delete(0, END)

    # Remove all the expenses
    def remove_all():
        for record in my_tree.get_children():
            my_tree.delete(record)

    # Remove one specific expense
    def remove_one():
        delete_selection = my_tree.selection()[0]
        my_tree.delete(delete_selection)

    # Buttons
    add_expenses = Button(root, text="Add your Expense", command=add_expenses)
    add_expenses.pack(pady=20)

    # remove all
    remove_all = Button(root, text="Remove all Expenses", command=remove_all)
    remove_all.pack(pady=10)

    # remove one
    remove_one = Button(root, text="Remove a specific expense", command=remove_one)
    remove_one.pack(pady=20)
    pass


button = Button(root, text='Submit', command=pressed, bg='medium sea green', fg='white')
button.pack(pady=10)


root.mainloop()
