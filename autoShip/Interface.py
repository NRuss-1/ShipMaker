import tkinter as tk
import BoatMath
import Instance


instanceData= Instance.InstanceData().getInstance()

def makeUI():
    window = tk.Tk()
    window.title("Ship Finder")
    window.geometry("300x250")

    text_label = tk.Label(window, text = "Enter the number of people you have")
    text_label.pack()
    text_entry = tk.Entry(window, width = 10)
    text_entry.pack()

    text_label2 = tk.Label(window, text = "Enter ship delimeter")
    text_label2.pack()
    text_entry2 = tk.Entry(window, width = 30)
    text_entry2.pack()

    pango = tk.IntVar()
    ares = tk.IntVar()
    hind = tk.IntVar()
    pango_button = tk.Checkbutton(window, text = "Show Pangolins!", variable=pango, onvalue=1, offvalue=0)
    ares_button = tk.Checkbutton(window, text = "Show Ares!", variable=ares, onvalue=1, offvalue=0)
    hind_button = tk.Checkbutton(window, text = "Show Hinds!", variable=hind, onvalue=1, offvalue=0)
    pango_button.pack()
    ares_button.pack()
    hind_button.pack()

    def get_input():
        text = text_entry.get()
        text2 = text_entry2.get()
        instanceData.initCombArr()
        instanceData.setNumPeople(int(text))
        instanceData.initPage()
        instanceData.setShips(pango.get(),ares.get(),hind.get())
        instanceData.setDelim(text2)
        BoatMath.createCompositions()
        lst = BoatMath.formatComps()
        displayValues(lst)

    submit_button = tk.Button(window, text = "Submit", command = get_input)
    submit_button.pack()

    window.mainloop()


class Table:
    def __init__(self, root, list):
        for i in range(len(list)):
            for j in range(len(list[0])):
                if (i == 0):
                    color = 'blue'
                else:
                    color = 'black'
                self.entry = tk.Entry(root, width = 15, fg = color, font = ('Arial', 11, 'bold'))
                self.entry.grid(row = i, column = j)
                self.entry.insert(tk.END, list[i][j])        


def displayValues(lst):
    window = tk.Tk()
    window.title("Ships!")

    def hit_next():
        instanceData.getNextPage()
        lst = BoatMath.formatComps()
        displayValues(lst)
    
    def hit_previous():
        instanceData.getPreviousPage()
        lst = BoatMath.formatComps()
        displayValues(lst)

    table = Table(window, lst)
    back_button = tk.Button(window, text = "Next", command = hit_next)
    back_button.place(relx=1.0, x = 0, y = 0, anchor = tk.NE)

    next_button = tk.Button(window, text = "Previous", command = hit_previous)
    next_button.place(x=0, y =0)

    window.mainloop()
