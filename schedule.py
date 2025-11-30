import random
from config_data import ACTIVITIES, ROOMS, ROOM_NAMES, TIME, TIME_MAP, FACILTATORS, EQUIPMENT_REQ, FAC_TIME_PREFS

class Schedule:
    def __init__(self):
        self.genes = {}
        self.fitness = 0.0 
        self.explain = []

    def initialization(self):
        """Create the initiliation of the population"""
        for activity in ACTIVITIES:
            r = random.choice(ROOM_NAMES)
            t = random.choice(TIME)
            f = random.choice(FACILTATORS)
            self.genes[activity] = (r, t, f)  # assign into the randomly generated tuple 
    
    def __str__(self):
        lines = []
        # format the output information
        lines.append(f"{"Activity" : < 10} | {"Room" : < 12} | {"Time" : < 6} | {"Faciltator"}") # put into lines to display
        lines.append("*" * 45)

        sort_genes = sorted(self.genes.items(), key=lambda x: (TIME_MAP[x[1][1]], x[1][0])) # creates a list of tuples that is sorted by time slot and room name 

        # format the output information
        for acts, (r, t, f) in sort_genes:
            lines.append(f"{acts:<10} | {r:<12} | {t:<6} | {f}")
        return "\n".join(lines)