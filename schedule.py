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
        """Print out the schedule output"""
        lines = []
        # format the output information
        lines.append(f"{"Activity" : < 10} | {"Room" : < 12} | {"Time" : < 6} | {"Faciltator"}") # put into lines to display
        lines.append("*" * 45)

        sort_genes = sorted(self.genes.items(), key=lambda x: (TIME_MAP[x[1][1]], x[1][0])) # creates a list of tuples that is sorted by time slot and room name 

        # format the output information
        for acts, (r, t, f) in sort_genes:
            lines.append(f"{acts:<10} | {r:<12} | {t:<6} | {f}")
        return "\n".join(lines)

def get_room_capacity(enrollment, capacity):
    """Calulates the score based on the room size"""
    used_space_rate = enrollment / capacity 
    if capacity < enrollment: 
        return -0.5
    elif used_space_rate >= 0.83:
        return +0.8
    elif used_space_rate >= 0.75:
        return +0.5
    elif used_space_rate >= 0.67:
        return +0.2
    elif used_space_rate >= 0.58:
        return -0.3
    else:
        return -0.6

def fitness_function(schedule, detail=False):
    score = 0.0 # intitial start
    genes = schedule.genes
    if detail: schedule.explain = [] # if true then clear the explain attribute into am empty list 

    def log(message, value):
        """Accumlate the fitness score & log records of how score was reached"""
        nonlocal score
        score += value 
        if detail: schedule.explain.append(f"{value:+.2f}: {message}") 
    room_time_map = {}
    fac_time_map = {}
    fac_total_load = {f: 0 for f in FACILTATORS} # tracks the total workload for each faciltator 
    fac_schedule  = {f: [] for f in FACILTATORS} # store the activites and time slots to specific faciltator 

    for acts, (r, t, f) in genes.items():
        time_index = TIME_MAP[t] 

        # populate the conflict maps 
        room_time_map.setdefault((r, t), []).append(acts) # any room key has more than on activity, raises room conflict
        fac_time_map.setdefault((f, t), []).append(acts) # any facilitator room key has more than one activity, raise faciltator conflict 

        # populate load maps
        fac_total_load[f] += 1
        fac_schedule[f].append({"Time Index" : time_index, "Room" : r, "Activity" : acts})

    for act, (r, t, f) in genes.items():
        # Takes care of room conflicts 
        if len(room_time_map[r, t]) > 1:
            log(f"Room Conflicts: {acts} shares a room {r} at {t}", -0.5)

        # Room Size
        capacity = ROOMS[r]['capacity']
        enrollment = ACTIVITIES[act]["enrollment"]
        size_score = get_room_capacity(enrollment, capacity)
        log(f"{act} room size in {r} ({capacity} vs {enrollment})", size_score)

        # Takes care of faciltators conflicts
        preferred = ACTIVITIES[act]['prefer']
        other = ACTIVITIES[act].get("others")

        if f in preferred:
            log(f"{act} overseen by preferred {f}", +0.5)
        elif f in other:
            log(f"{act} overseen by other listed {f}", +0.2)
        else:
            log(f"{act} overseen by unlisted {f}", -0.1)
            