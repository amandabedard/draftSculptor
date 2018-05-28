#Amanda Bedard, 2018
#A simple UI for the app

from tkinter import *
import draftSculptor

ESSAYOPTIONS={'Opinion', 'Reflection'}

def start():
    #Populate the essay box
    def makeEssay():
        eoutline = outline.get()
        eessayType = essaytype.get()
        fluffy = fluff.get()
        if fluffy == 1:
            fluffy = True
        else:
            fluffy = False
        essay.delete("1.0", END)
        essay.insert(END, draftSculptor.sculptDraft(eoutline, eessayType, fluffup=fluffy))

    #Configure the UI
    master = Tk()
    master.title("DraftSculptor")
    Label(master, text="DraftSculptor Essay Draft Generator").grid(row=0)
    Label(master, text="").grid(row=1)
    Label(master, text="Outline file: ").grid(row=2, column=0, sticky=W, pady=4)
    Label(master, text="Essay Type: ").grid(row=3, column=0, sticky=W, pady=4)
    Label(master, text="Template: ").grid(row=5, column=0, sticky=W, pady=4)
    Label(master, text="Padding Text: ").grid(row=6, column=0, sticky=W, pady=4)
    Label(master, text="").grid(row=7)
    Label(master, text="<Not yet supported>").grid(row=5, column=0)

    outline = Entry(master)
    outline.insert(END,'sampleDocs/outline.txt')
    essaytype= StringVar()
    box = OptionMenu(master, essaytype, ESSAYOPTIONS).grid(row=3, column=0)
    essaytype.set('Opinion')
    fluff = IntVar()
    Checkbutton(master, variable=fluff).grid(row=6, column=0)
    essay = Text(master, wrap=WORD)

    outline.grid(row=2, column=0)
    essay.grid(row=9)

    Button(master, text='Compose Essay', command=lambda : makeEssay()).grid(row=8, column=0, pady=4)

    mainloop()

if __name__ == '__main__':
    start()