#Amanda Bedard, 2018
#A simple UI for the app

from tkinter import *
from draftSculptor import sculptDraft

def start():
    #Populate the essay box
    def makeEssay():
        eoutline = outline.get()
        eessayType = essaytype.get()
        essay.delete("1.0", END)

        essay.insert(END, sculptDraft(eoutline, eessayType))

    #Configure the UI
    master = Tk()
    master.title("DraftSculptor")
    Label(master, text="DraftSculptor Essay Draft Generator").grid(row=0)
    Label(master, text="").grid(row=1)
    Label(master, text="Outline file: ").grid(row=2, column=0, sticky=W, pady=4)
    Label(master, text="Essay Type: ").grid(row=3, column=0, sticky=W, pady=4)
    Label(master, text="Template: ").grid(row=5, column=0, sticky=W, pady=4)
    Label(master, text="").grid(row=6)
    Label(master, text="<Not yet supported>").grid(row=5, column=0)

    outline = Entry(master)
    outline.insert(END,'sampleDocs/outline.txt')
    essaytype = Entry(master)
    essaytype.insert(END, 'opinion')
    essay = Text(master, wrap=WORD)

    outline.grid(row=2, column=0)
    essaytype.grid(row=3, column=0)
    essay.grid(row=8)

    Button(master, text='Compose Essay', command=lambda : makeEssay()).grid(row=7, column=0, sticky=W, pady=4)

    mainloop()

if __name__ == '__main__':
    start()