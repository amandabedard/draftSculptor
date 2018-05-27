#File for composing the draft based on the type of essay
from json import load
import random

def fluffGetter(fname):
    f = open(fname, 'r')
    data = load(f)
    return data

#Function to select the correct style of essay
def draftChooser(essayType, draftData):

    if essayType == 'Opinion':
        print(opinionEssay(draftData))
    else:
        print("Sorry, that format is not currently supported")

#Function to draft an opinion essay
def opinionEssay(data):
    #Get the fluff for formatting the essay and prepare the essay string
    FLUFF = 'essayFluff/opinion_transitions_1.json'
    essayStr = ''
    essayfluff = fluffGetter(FLUFF)
    essayStr += introComposer("A BIG FANCY POINT", ["DETAIL 1", "DETAIL 2"], essayfluff['intro'])
    print(essayStr)

def introComposer(point, topics, fluff):
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

    rnd = random.randrange(0, len(fluff['3']))  
    intro += fluff['3'][rnd]
    intro += '\n'
    return intro

    



print(opinionEssay(None))