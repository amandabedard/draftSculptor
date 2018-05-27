#File for reading and interpreting the outline

#Function to read the draft from a file
def readDraft(fname):
    f = open(fname, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

#Function to parse the draft and create a dict with relevant data
def parseDraft(lines):
    #Some variables for keeping track of the topics and the dict object
    outlineDict = {
        'title': ''
        }
    currentTopic = ''
    subtopic = ''

    #Now, let's parse the data
    try:
        for line in lines:
            if line[0] == '#':
                outlineDict['title'] = line[1:len(line)]
            elif line[0] == '>':
                outlineDict[line[1:len(line)]] = {}
                currentTopic = line[1:len(line)]
            elif line[0] == '<':
                outlineDict[currentTopic][line[1:len(line)]] = []
                subtopic = line[1:len(line)]
            elif line[0] == '-':
                outlineDict[currentTopic][subtopic].append(line[1:len(line)])
            #Something is wrong with the formatting, raise an exception
            else:
                raise

        return outlineDict
    #An exception was raised while reading the draft, something needs to be fixed
    except:
        print("There is an error with the draft format. Please check your outline and try again.")
