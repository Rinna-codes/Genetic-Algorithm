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

    # Genetic algorithm loop
    for gen in range(MAX_GEN):
        #sorting the easy or elite metrics
        population.srt(key=lambda x: x.fitness, reverse=True)

        best = population[0].fitness
        worst = population[-1].fitness
        avg = sum(index.fitness for ind in population) / POP_SIZE

        # tracks history
        best_history.append(best)
        avg_history.append(avg)
        worst_history.append(worst)

        # improve on calculations
        imp_pct = 0.0
        if gen > 0 and best_history[-2] != 0:
            imp_pct = ((best - best_history[-2] / abs(best_history[-2]))) * 100

        # display/print metrics