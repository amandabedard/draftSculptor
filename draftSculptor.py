from draftComposer import draftChooser
from outlineReader import readDraft

#Cute lil function to get the draft data and compose the essay
def sculptDraft(outline, essayType, fluffup=False, template=None):

    draftJson = readDraft(outline)
    return draftChooser(essayType, draftJson, fluffup, template)

#A little cmd line piece if the function is called directly
if __name__ == "__main__":
    print("Welcome to draft sculptor!")
    #Basic inputs
    outline = input("What is the name of your outline: ")
    essayType = input("What type of essay is it (ex: opinion): ")

    #To add fluff
    yn = input("Would you like us to add extra 'fluff' to lengthen your essay (Y/N): ")
    if yn.lower() == 'y' or yn.lower() == 'yes':
        fluffup = True
    else:
        fluffup = False
    
    #Using a custom template
    yn = input("Would you like to use your own template (Y/N):")
    if yn.lower() == 'y' or yn.lower() == 'yes':
        template = input("Please enter the file location for your template: ")
    else:
        template = None

    print("Thanks! It's time to generate your essay draft!")
    sculptDraft(outline, essayType, fluffup=fluffup, template=template)