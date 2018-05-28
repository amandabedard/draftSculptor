#Amanda Bedard, 2018
#File for composing the draft based on the type of essay
from json import load
from outlineReader import readDraft
import random

#Function to load essay 'fluff' json template
def fluffGetter(fname):
    f = open(fname, 'r')
    data = load(f)
    return data

#Function to select the correct style of essay
def draftChooser(essayType, draftData, fluffup=False, template=None):

    if essayType.lower() == 'opinion':
        if not template:
            return opinionEssay(draftData, fluffup=fluffup)
        else:
            return opinionEssay(draftData, fluffup=fluffup, template=template)
            
    else:
        print("Sorry, that format is not currently supported")

#Function to draft an opinion essay
def opinionEssay(data, fluffup=False, template='essayTemplates/opinion_transitions_1.json'):
    #Get the fluff for formatting the essay and initialize the essay string
    print("Preparing your opinion essay, please wait..")
    essayStr = ''
    xtra = None
    essayfluff = fluffGetter(template)

    #Get a few extra variables from the data
    topic = data['title']
    details = [k for k, v in data['data'].items()]
    ixtra = None
    bxtra = None
    cxtra = None
    if fluffup:
        ixtra = essayfluff["xfluff"]['intro']
        bxtra = essayfluff["xfluff"]['body']
        cxtra = essayfluff["xfluff"]['conclusion']


    #Begin composing the essay, with the introduction
    essayStr += firstlastComposer(topic, details, essayfluff['intro'], xtra=ixtra)
    
    #Now, the body paragraphs
    paragraphs = len(details) + 1
    count = 1
    for detail in details:
        if count == 1:
            essayStr += composebody("1", detail, data['data'][detail], essayfluff['topic'], essayfluff['details'], xtra=bxtra)
        elif count == paragraphs:
            essayStr += composebody("3", detail, data['data'][detail], essayfluff['topic'], essayfluff['details'], xtra=bxtra)
        else:
            essayStr += composebody("2", detail, data['data'][detail], essayfluff['topic'], essayfluff['details'], xtra=bxtra)
        count += 1

    #Finally, the conclusion paragraph
    essayStr += firstlastComposer(topic, details, essayfluff['conclusion'], xtra=cxtra)

    #Essay is done! Time to save.
    print("Finished composing the essay!")
    saveEssay(essayStr)

    return essayStr

#Function to save the essay to a file location or default the current directory
def saveEssay(essayStr, filelocation='./'):
    try:
        print("Saving file, please wait..")
        f = open((filelocation + 'draft.txt'), 'w')
        f.write(essayStr)
        f.close()
        print("Save Successful! File saved at %sdraft.txt" % (filelocation))
    except:
        print("Save Failure.  Please try again.")

#Function to compose a generic introductory or conclusion paragraph    
def firstlastComposer(point, topics, fluff, xtra=None):
    intro = '    '

    #Start with an introductory sentence
    rnd = random.randrange(0, len(fluff['1']))  
    intro += (fluff['1'][rnd] % point).capitalize().replace(' i ', ' I ')

    #Now list the topics of discussion
    rnd = random.randrange(0, len(fluff['2']))
    topicstr = ''
    for topic in topics:
        if topics[-1] == topic:
            topicstr += ('and %s' % topic)
        else:
            topicstr += ('%s, ' % topic)
    intro += (fluff['2'][rnd] % topicstr).capitalize().replace(' i ', ' I ')

    if xtra:
        rnd = random.randrange(0, len(xtra))
        intro += xtra[rnd]

    #Close it out!
    rnd = random.randrange(0, len(fluff['3']))  
    intro += (fluff['3'][rnd]).capitalize().replace(' i ', ' I ')
    intro += '\n'
    return intro

#Function to compose a generic body paragraph
def composebody(num, detail, substance, fluff, dfluff, xtra=None):
    body = '    '
    subtopics = [k for k, v in substance.items()]

    #The transition statement
    rnd = random.randrange(0, len(fluff[num]))  
    body += (fluff[num][rnd] % detail).capitalize().replace(' i ', ' I ')

    for topic in subtopics:
        #Add the topics to the body.
        rnd = random.randrange(0, len(dfluff))  
        body += (dfluff[rnd] % topic).capitalize().replace(' i ', ' I ')
        #Fill in the finer details
        if substance[topic] != []:
            for deet in substance[topic]:
                body += '%s. ' % deet.capitalize().replace(' i ', ' I ')
        else:
            rnd = random.randrange(0, len(xtra))
            body += xtra[rnd]

    #Newline at the end of the paragraph, then send it back!
    body += '\n'
    return body

#opinionEssay(readDraft('outline.txt'))
