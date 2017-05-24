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
IDEA Add some prayers too, would likely be less generated
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

# creates news associated with the mechanicum
def mechanicus_message():
    pick = random.randint(1,4)
    if pick == 1:
        return("After recent damage caused by attacks from the " + random.choice(enemies) + ", sector " + str(random.randint(1,100)) + " of planet " + random.choice(planets) + " will be partially uninhabitable for the next " + str(random.randint(2,40)) + " months. The Mechanicus apologies for any inconvenience caused.")
    elif pick == 2:
        return("Due to unexpectedly high levels of radiation leakage on " + random.choice(planets) + ", mutations are unacceptably high and nearby " + random.choice(chapters) + " are inbound for purification. The Mechanicus apologies for any inconvenience caused.")
    elif pick == 3:
        return("Mechanicus servitor stock low on " + random.choice(planets) + ", good prices paid to the families of the chosen.")
    else:
        return("Technologically gifted individuals on " + random.choice(planets) + ", the Mechanicus have been asked to fill roles of chapter serfs in the " + random.choice(chapters) + " as soon as the Emperor will allow.")

# announcements related to current warp activity for travel
def warp_travel():
    pick = random.randint(1,4)
    if pick == 1:
        return("Due to recent warp-storms and local heresy, warp travel between " + random.choice(planets) + " and " + random.choice(planets) + " is now unadvisable. May the Emperor protect.")
    elif pick == 2:
        return("A large warp-rift has been detected in the system of the planet " + random.choice(planets) + ". Avoid if possible, " + random.choice(chapters) + " astartes have been dispatched.")
    elif pick == 3:
        return("After abation of recent warp-storms, travel has been re-instated around " + random.choice(planets) + ", caution still advised.")
    else:
        return("Astropathic contact has been lost with " + random.choice(planets) + ", " + random.choice(planets) + " and " + random.choice(planets) + ". We will give updates if they occur.")

# recuitment ads for various groups
def recruitment():
    pick = random.randint(1,4)
    if pick == 1:
        return("Want to see the galaxy, prove your faith and get paid? Imperial Guard recruitment tents now open in sector " + str(random.randint(1,100)) + " on " + random.choice(planets) + ". Sign up today!")
    elif pick == 2:
        return("After recent " + random.choice(enemies) + " attacks, significant openings in the " + random.choice(planets) + " planetary defence forces must be filled. Successful applicants will also receive a free subscription to the Imperial Times.")
    elif pick == 3:
        return(random.choice(chapters) + " recruitment officers en-route to " + random.choice(planets) + ", sector " + str(random.randint(1,100)) + ". Seek out Captain " + random.choice(names) + " to begin testing, unsuccessful initiates will be given servitor servitude.")
    else:
        return("Imperial Guard regiment " + str(random.randint(1,100)) + " on " + random.choice(planets) + " are now recruiting in sector " + str(random.randint(1,100)) + " for infantry and sector " + str(random.randint(1,100)) + " for mobile armour positions. A complimentary lasgun and flak vest will be provided.")

# news of civil disturbances and suppression    
def civil_unrest():
    pick = random.randint(1,4)
    if pick == 1:
        return("Sector " + str(random.randint(1,100)) + " of " + random.choice(planets) + " will now be subject to a 9pm Terran standard curfew due to recent outbreaks of civil unrest.")
    elif pick == 2:
        return("After the loss of a fleet of cargo ships, the Administratum assures us there will be no food shortages on " + random.choice(planets) + ", Arbites will be deployed to ensure civilian saftey.")
    elif pick == 3:
        return("Rioting in sector " + str(random.randint(1,100)) + " of " + random.choice(planets) + " has forced the deployment of local Guard forces for suppression. The Emperor protects those who protect themselves.")
    else:
        return("Due to an unknown pathogen on a nearby agri-world, food prices are set to double on " + random.choice(planets) + ", additional Arbites forces will be deployed to supress dissatisfied subjects.")

# news concerning the original traitor legions and their actions
def traitor_marines():
    pick = random.randint(1,4)
    if pick == 1:
        return("A large fleet of the " + random.choice(traitors) + " traitor legion has been detected near " + random.choice(planets) + ". Emperor give you strength for the horrors you will endure.")
    elif pick == 2:
        return("Stray elements of the " + random.choice(traitors) + " have been eradicated by a fleet from the " + random.choice(chapters) + ". His will be done.")
    elif pick == 3:
        return("Due to recent allegeded contact between the planetary goverment of " + random.choice(planets) + " and operatives of the traitor " + random.choice(traitors) + ", the Inquition has grounded all orbital flights and transfers.")
    else:
        return("" + random.choice(traitors) + " legionaries have been routed from sector " + str(random.randint(1,100)) + " of planet " + random.choice(planets) + ", precautionary civil executions may follow to ensure the purity of the populace.")

'''
New types of news functions in progress

# returns a random prayer from the txt file
def prayer():
    return(random.choice(prayers))
'''
    
# list of tweet types and a function to pick which type of news to tweet
# needed by tweeter module, DO NOT change below here without thinking
# and add new news types to the array as required
tweet_types = [obituary, new_marine, marine_promotion, battle_report, mechanicus_message, warp_travel, recruitment, civil_unrest, traitor_marines]

def tweet_news():
    return(random.choice(tweet_types)())

# keep all list variables here
names = import_list("Name")
planets = import_list("Planet")
chapters = import_list("Chapter")
roles = import_list("Role")
enemies = import_list("Enemy")
ranks = import_list("Rank")
traitors = import_list("Traitor Legion")
# yet to use
prayers = import_list("Prayer")
