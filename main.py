# Main execution file 
import copy
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
        population.sort(key=lambda x: x.fitness, reverse=True)

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
        if gen % 10 == 0 or gen == MAX_GEN -1 or gen == 0:
            print(f"{gen:<5} | {best:<8.2f} | {avg:<8.2f} | {worst:<8.2f} | {imp_pct:<8.2f} | {mutation_rate:.5f}")
        # Adaptive mutation + stopping criteria 
        if best > best_fintess_global + 1e-6:
            best_fintess_global = best
            generations_without_improve = 0
        else:
            generations_without_improve += 1
        
        # halve mutaiton if stagnant
        if generations_without_improve >= THRESHOLD and mutation_rate > 1e-5:
            mutation_rate /= 2
            generations_without_improve = 0
        
        # stopping rule: Have to run 100 generations THEN check for greater than 1% average improvement
        if gen >= 100:
            window = 20
            if len(avg_history) >= window:
                avg_start = avg_history[-window]
                avg_current = avg_history[-1]

                avg_improvement_pct = 0.0
                if avg_start != 0:
                    avg_improvement_pct ==((avg_current -avg_start) / abs(avg_start)) * 100
                
                if avg_improvement_pct < 1.0 and avg_current >= avg_start:
                    print(f"\nStopping Criteria was Met! Average fitness improvement ({avg_improvement_pct:.2f}%) over last {window} generationsis less than 1%.")
                    break

    # Reproduction (crossover + mutate)
    next_generation = []
    
    # Take the top 5%
    num_elites = max(1, int(POP_SIZE * 0.05))
    for i in range(num_elites):
        next_generation.append(copy.deepcopy(population[i]))
    
    while len(next_generation) < POP_SIZE:
        parents = softmax_selection(population, 2)
        child = crossover(parents[0], parents[1])
        mutate(child, mutation_rate)
        child.fitness = fitness_function(child)
        next_generation.append(child)
    
    population = next_generation

    # Saving the report 
    population.sort(key=lambda x: x.fitness, reverse=True)
    final_best = population[0]

    # claculate the best schdeule 
    fitness_function(final_best, detail=True)

    print_chart(best_history, avg_history, worst_history)

    print("\n" + "=" * 30)
    print("FINAL BEST SCHEDULE")
    print("=" * 30)
    print(final_best)
    print(f"\nFINAL FITNESS: {final_best.fitness:.2f}")

    save_report(final_best, best_history, avg_history, worst_history)

if __name__ == "__main__":
    main()