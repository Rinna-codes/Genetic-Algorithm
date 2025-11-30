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
            r = random