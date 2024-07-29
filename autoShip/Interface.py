import tkinter as tk
import BoatMath
import Instance

instanceData = Instance.InstanceData()

def makeUI():
    window = tk.Tk()
    window.title("Ship Finder")
    window.geometry("300x150")

    text_label = tk.Label(window, text = "Enter the number of people you have")
    text_label.pack()
    text_entry = tk.Entry(window, width = 10)
    text_entry.pack()
    def get_input():
        text = text_entry.get()
        instanceData.initCombArr()
        instanceData.setNumPeople(int(text))
        instanceData.initPage()
        BoatMath.createCompositions(int(text), instanceData)
        lst = BoatMath.formatComps(instanceData)
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
        lst = BoatMath.formatComps(instanceData)
        displayValues(lst)
    
    def hit_previous():
        instanceData.getPreviousPage()
        lst = BoatMath.formatComps(instanceData)
        displayValues(lst)

    table = Table(window, lst)
    back_button = tk.Button(window, text = "Next", command = hit_next)
    back_button.place(relx=1.0, x = 0, y = 0, anchor = tk.NE)

    next_button = tk.Button(window, text = "Previous", command = hit_previous)
    next_button.place(x=0, y =0)

    window.mainloop()