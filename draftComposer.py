#File for composing the draft based on the type of essay
from json import load
import random

def fluffGetter(fname):
    f = open(fname, 'r')
    data = load(f)
    return data

#Function to select the correct style of essay
def draftChooser(essayType, draftData, fluffup=False):

    if essayType == 'Opinion':
        print(opinionEssay(draftData, fluffup=fluff))
    else:
        print("Sorry, that format is not currently supported")

#Function to draft an opinion essay
def opinionEssay(data, fluffup=False):
    #Get the fluff for formatting the essay and prepare the essay string
    FLUFF = 'essayFluff/opinion_transitions_1.json'
    essayStr = ''
    xtra = None
    essayfluff = fluffGetter(FLUFF)
    essayStr += introComposer("A BIG FANCY POINT", ["DETAIL 1", "DETAIL 2"], essayfluff['intro'])
    saveEssay(essayStr)

def saveEssay(essayStr, filelocation='./'):
    try:
        print("Saving file, please wait..")
        f = open((filelocation + 'draft.txt'), 'w')
        f.write(essayStr)
        f.close()
        print("Save Successful!")
    except:
        print("Save Failure.  Please try again.")
    

def introComposer(point, topics, fluff, xtra=None):
    intro = '    '

    rnd = random.randrange(0, len(fluff['1']))  
    intro += fluff['1'][rnd] % point

    rnd = random.randrange(0, len(fluff['2']))
    topicstr = ''
    for topic in topics:
        if topics[-1] == topic:
            topicstr += ('and %s' % topic)
        else:
            topicstr += ('%s, ' % topic)
    intro += fluff['2'][rnd] % topicstr

    if xtra:
        rnd = random.randrange(0, len(xtra))

    rnd = random.randrange(0, len(fluff['3']))  
    intro += fluff['3'][rnd]
    intro += '\n'
    return intro

    



print(opinionEssay(None))