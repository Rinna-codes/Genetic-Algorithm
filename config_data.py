"""Configuration + Scheduling Data File"""

"""Main Configurations + Constraints"""

POP_SIZE = 500 
MAX_GEN = 500
STARTING_MUT_RATE = 0.01
THRESHOLD = 20 # Generations that don't have improvement before mutation 

OUTPUT_FILE = "schedule_output.txt"

"""Definitions following Appendix A"""
ACTIVITIES = {
    "SLA101A" : {"enrollment": 40, "prefer" : ["Glen", "Lock", "Banks"], "others" : ["Numen", "Richards", "Shaw", "Singer"]}, 
    "SLA101B" : {"enrollment" : 35, "prefer" : ["Glen", "Lock", "Banks"], "others" : ["Numen", "Richards", "Shaw", "Singer"]},
    "SLA191A" : {"enrollment": 45, "prefer" : ["Glen", "Lock", "Banks"], "others" : ["Numen", "Richards", "Shaw", "Singer"]},
    "SLA191B" : {"enrollment" : 40, "prefer" : ["Glen", "Lock", "Banks"], "others" : ["Numen", "Richards", "Shaw", "Singer"]},
    "SLA201" : {"enrollment" : 60, "prefer" : ["Glen", "Banks", "Zeldin", "Lock", "Singer"], "others" : ["Richards", "Uther", "Shaw"]},
    "SLA291" : {"enrollment" : 50, "prefer" : ["Glen", "Banks", "Zeldin", "Lock", "Singer"], "others" : ["Richards", "Uther", "Shaw"]},
    "SLA303" : {"enrollment": 25, "prefer" : ["Glen", "Zeldin"], "others" : ["Banks"]},
    "SLA304" : {"enrollment" : 20, "prefer" : ["Singer", "Uther"], "others" : ["Richards"]},
    "SLA394" : {"enrollment" : 15, "prefer" : ["Tyler", "Singer"], "others" : ["Richards", "Zeldin"]},
    "SLA449" : {"enrollment" : 30, "prefer" : ["Tyler", "Zeldin", "Uther"], "others" : ["Zeldin", "Shaw"]},
    "SLA451" : {"enrollment" : 90, "prefer" : ["Lock", "Banks", "Zeldin"], "others" : ["Tyler", "Singer", "Shaw", "Glen"]}
}

ROOMS = {
    "Beach 201" : {"capacity" : 18, "lab" : False, "projector" : True, "grouping" : True},
    "Beach 301" : {"capacity" : 25, "lab" : True, "projector" : True, "grouping" : True},
    "Frank 119" : {"capacity" : 95, "lab" : True, "projector" : True, "grouping" : False},
    "Loft 206" : {"capacity" : 55, "lab" : False, "projector" : False, "grouping" : False},
    "Loft 310" : {"capacity" : 48, "lab" : True, "projector" : False, "grouping" : False},
    "James 325" : {"capacity" : 110, "lab" : True, "projector" : True, "grouping" : False},
    "Roman 201" : {"capacity" : 40, "lab" : False, "projector" : False, "grouping" : True},
    "Roman 216" : {"capacity" : 80, "lab" : True, "projector" : True, "grouping" : True},
    "Slatter 003" : {"capacity" : 32, "lab" : True, "projector": True, "grouping" : False}
}

ROOM_NAMES = list(ROOMS.keys()) # Turns the dictionary keys into a list
TIME = ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"]
TIME_MAP = {time: index for index, time in enumerate(TIME)} # Number indexes the times
FACILTATORS = ["Lock", "Glen", "Banks", "Richards", "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]

# Equipment Requirements : {Acivity Name: (Needs a lab, Needs a projector)}
EQUIPMENT_REQ = {
    "SLA304" : (True, False),
    "SLA303" : (True, True),
    "SLA191" : (True, False),
    "SLA291" : (True, False),
    "SLA449" : (False, True),
    "SLA451" : (True, True)
}

# The faciltators Time Slot preferences 
FAC_TIME_PREFS = {
    "Glen" : {"likes" : ["10 AM", "11 AM"], "avoid" : ["3 PM"]},
    "Banks" : {"likes" : ["10 AM", "12 PM"], "avoid" : ["11 AM", "1 PM"]},
    "Tyler" : {"likes" : ["2 PM", "3 PM"], "avoid" : ["10 AM", "11 AM"]},
    "Singer" : {"avoid" : ["12 PM"]}
}