# Main execution file 

from config_data import POP_SIZE, MAX_GEN, STARTING_MUT_RATE, THRESHOLD
from schedule import Schedule, fitness_function, softmax_selection, crossover, mutate
from report import print_chart, save_report

def main():
    # Starting menu+message
    print(f"---SLA GENETIC SCHEDULER---")
    print(f"POPULATION SIZE: {POP_SIZE}, MAX GENERATIONS {MAX_GEN}")
    print("Initializing population...")

    # The initialization
    population = []
    for _ in range(POP_SIZE):
        index = Schedule()
        index.initialization()
        index.fitness = fitness_function(index)
        population.append(index)

    mutation_rate = STARTING_MUT_RATE
    best_history = []
    avg_history = []
    worst_history = []

    generations_without_improve = 0 
    best_fintess_global = -float('inf')

    print(f"\n {'GENERATIONS':<5} | {"BEST":<8} | {"AVERAGE":<8} | {"WORST":<8} | {"IMP %":<8} | {"MUTATE RATE"}")
    print("-" * 60)