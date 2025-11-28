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
    "SLA101B" : {"enrollment" : 35, "prefer" : ["Glen", "Lock", "Banks"], "others" : ["Numen", "Richards", "Shaw", "Singer"]}
}