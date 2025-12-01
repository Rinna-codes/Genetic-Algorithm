import datetime
from config_data import OUTPUT_FILE

def print_chart(best_history, avg_history, worst_history):
    """Create the CLI chart for Best, Average, and Worst fitness scores"""
    if not best_history: 
        print("\nNot enough data to make chart")
        return 

    # Formatting for printing the chart 
    print("\n" + "=" * 60)
    print("FITNESS HISTORY CHART")
    print("Legend: #=Best, +=Average, -=Worst")
    print("=" * 60)

    # Variables for the matrix to contain the history marks 
    height = 15 
    width= 60 

    values_sum = best_history + avg_history + worst_history
    max_value = max(values_sum)
    min_value = min(values_sum)
    value_range = max_value - min_value if max_value != min_value else 1.0

    # Empty 2d list to contained the history fitness marks
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    num_generations = len(best_history)
    step_interval = num_generations / width if num_generations > width else 1.0

    for col in range(width):
        index = int(col * step_interval) # Corresponds the col index to the index in the history list
        if index >= num_generations:
            break

        # Normalize the fitness scores into standardized range  
        def normal(value):
            if value_range == 1.0 and max_value == min_value: 
                return 0.5
            return (value - min_value) / value_range
        
        norm_b = normal(best_history[index])
        norm_a = normal(avg_history[index])
        norm_w = normal(worst_history[index])

        row_b = max(0, min(height-1), int(norm_b * (height-1)))
        row_a = max(0, min(height-1), int(norm_a * (height-1)))
        row_w = max(0, min(height-1), int(norm_w * (height-1)))

        # plotting for best, average, and worst 
        grid[height - 1 - row_w][col] = "-"
        grid[height - 1 - row_a][col] = "+"
        grid[height - 1 - row_b][col] = "#"
    
    # Displaying the chart
    print(f"{max_value:>6.2f} |", end="")
    print("-" * width)
    for i, row in enumerate(grid):
        print(f"{'':>6.2f} " + "".join(row))
    
    print(f"{min_value:>6.2f} |", end="")
    print("-" * width)
    print(f"{'':>6} 0" + " "*(width-10) + f"{num_generations} Generations")


def report(final_best, best_history, avg_history, worst_history):
    """Saves the report and best schedule to an output file"""
    with open(OUTPUT_FILE, "w") as f: 
        
        # Summary of the schedule results 
        f.write("--- SLA SCHEDULE GENETIC ALGORITHM RESULTS ---\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Generations Run: {len(best_history)}\n")
        f.write(f"Ginal Fitness Score: {final_best:.2f}\n\n")
        
        f.write("---SCHEDULE---\n")
        f.write(str(final_best))

        f.write("\n\n---SCORE BREAKDOWN (CONSTRAINT VOLATIONS) ---\n")
        for line in final_best.explaination:
            f.write(line + "\n")
        
        f.write("\n\n---GENERATION HISOTRY---\n")
        f.write("GENERATION, BEST, AVERAGE, WORST\n")
        for i in range(len(best_history)):
            f.write(f"{i}, {best_history[i]:.4f}, {avg_history[i]:.4f}, {worst_history[i]:.4f}\n")

    print(f"\nRESULTS SAVED TO {OUTPUT_FILE}")