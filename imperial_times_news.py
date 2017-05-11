'''
Python script to generate random warhammer "tweets" for use in the imperial times twitterbot
This to be imported to the tweeter for use, this to create news and add variety
'''

# module needed to pick randomly from a list
import random
# import time and take a random seed?

# converts a .txt file of the same name to an iterable list in python
def import_list(var):
    with open(var+".txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    return content


'''
IDEA Mechanicus maintance in sectors and certain things broken
IDEA Severe weather/warp-storm warnings for some places
IDEA Curfews and other civil disturbances, riots etc
IDEA Recruitment for guardsman and PDF?
IDEA Add some prayers too, would likely be less generated
IDEA traitor legion incursion? sorry and a prayer
IDEA go over and use roles more?
IDEA append roman numerals to planets in txt list when updated
'''

# random obituary for a high-ranking marine
def obituary():
    pick = random.randint(1,5)
    if pick == 1:
        return("Today we mourn the death of " + random.choice(ranks) + " " + random.choice(names) + " of the " + random.choice(chapters) + ". Who died fighting " + random.choice(enemies) + " on " + random.choice(planets) + ".")
    elif pick == 2:
        return("Let this day mark the loss of " + random.choice(ranks) + " " + random.choice(names) + ", granted the Emperors peace in the field of battle on " + random.choice(planets) + ".")
    elif pick == 3:
        return("Contact has been lost with a squad of the " + random.choice(chapters) + " since a recent warp-translation to battle " + random.choice(enemies) + " on " + random.choice(planets) + ", may they find peace where ever they are.")
    elif pick == 4:
        return("A sneak-incursion by " + random.choice(enemies) + " on " + random.choice(planets) + " has taken the life of " + random.choice(ranks) + " " + random.choice(names) + " from the " + random.choice(chapters) + ". Only in death does duty end.")
    else:
        return("As of last night, we have recieved reports of the summary execution of " + random.choice(ranks) + " " + random.choice(names) + " of the " + random.choice(chapters) + " for heresy and lack of faith.")

# random bio for a newly initiated marine
def new_marine():
    pick = random.randint(1,4)
    if pick == 1:
        return("Hail new marine " + random.choice(names) + " born from " + random.choice(planets) + ". He joins his brothers from the " + random.choice(chapters) + " in the " + random.choice(roles) + " squads.")
    elif pick == 2:
        return(random.choice(names) + " joins the " + random.choice(chapters) + " upon completion of the necessary rites of initiation on " + random.choice(planets) + ". May death come swiftly to all who meet him in battle.")
    elif pick == 3:
        return("From the world of " + random.choice(planets) + ", congratulations to " + random.choice(names) + " for surviving the trials and becoming a full battle-brother in the " + random.choice(chapters) + ".")
    else:
        return(random.choice(names) + " has recieved his black carapace to join the ranks for the " + random.choice(chapters) + " under the tutelage of their " + random.choice(roles) + " Sergeant.")

# generates news of a promotion of a marine
def marine_promotion():
    pick = random.randint(1,4)
    if pick == 1:
        return("In His glorious name, it is henceforth decreed " + random.choice(names) + " from the " + random.choice(chapters) + " be promoted to the rank of " + random.choice(ranks) + ".")
    elif pick == 2:
        return("Due to battlefield losses on " + random.choice(planets) + ", the " + random.choice(chapters) + " have elevated " + random.choice(names) + " to the rank of " + random.choice(ranks) + ".")
    elif pick == 3:
        return("A report within the last terran standard day has announced an appointment in the " + random.choice(chapters) + " of " + random.choice(ranks) + " " + random.choice(names) + ".")
    else:
        return("After valiant efforts against the " + random.choice(enemies) + ", " + random.choice(names) + " of the " + random.choice(chapters) + " will be given the rank of " + random.choice(ranks) + ".")

# generates a simple battle-report
def battle_report():
    pick = random.randint(1,4)
    if pick == 1:
        return("A great victory was achieved by the " + random.choice(chapters) + " against the " + random.choice(enemies) + " on " + random.choice(planets) + ".")
    elif pick == 2:
        return("A seige on " + random.choice(planets) + " was recently broken by the " + random.choice(chapters) + " and the planet was returned to Imperial rule, residual purges may be required locally.")
    elif pick == 3:
        return("A battle-force of " + random.choice(chapters) + " were forced to abandon " + random.choice(planets) + " due to irreparable taint from the " + random.choice(enemies) + ", exterminatus expected.")
    else:
        return("A thorough clensing of " + random.choice(planets) + " was undertaken by the " + random.choice(chapters) + " led by a local Inquisitor, due to alleged Chaos infection.")

# returns a random prayer from the txt file
def prayer():
    return(random.choice(prayers))


'''
New types of news functions in progress

def mechanicus_message():
    return()
    
def warp_travel():
    return()
    
def recruitment():
    return()
    
def civil_unrest():
    return()

def traitor_marines():
    return()
    #
'''


    
# list of tweet types and a function to pick which type of news to tweet
# needed by tweeter module, DO NOT change below here without thinking
# and add new news types to the array as required
tweet_types = [obituary, new_marine, marine_promotion, battle_report, prayer]

def tweet_news():
    return(random.choice(tweet_types)())



# keep all list variables here
names = import_list("Name")
planets = import_list("Planet")
chapters = import_list("Chapter")
roles = import_list("Role")
enemies = import_list("Enemy")
ranks = import_list("Rank")
prayers = import_list("Prayer")
# yet to use
traitor_legions = import_list("Traitor Legion")
