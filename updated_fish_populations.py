import matplotlib.pyplot as plt

def calculate_fish_population(initial_fish_population, carrying_capacity, growth_rate):
    """Calculate the fish population at each year based on the initial population, carrying capacity, and growth rate."""
    return initial_fish_population + growth_rate * initial_fish_population * (1 - (initial_fish_population / carrying_capacity))

# growth rate
r = 0.05

# initial number of fish
initial_fish_population = float(input("Input the initial number of fish: "))

# carrying capacity
carrying_capacity = float(input("Input the carrying capacity of the fish population: "))

# number of years to project for
years = float(input("Input the number of years to be modelled: "))

# validate input values
if initial_fish_population < 0 or carrying_capacity < 0 or years < 0:
    print("Error: Please input positive values for the initial fish population, carrying capacity, and number of years.")
    exit()

# list to store fish population for each year
fish_populations = []

# calculate fish population for each year and store in list
for i in range(1, years + 1):
    fish_populations.append(calculate_fish_population(initial_fish_population, carrying_capacity, r))
    initial_fish_population = fish_populations[-1]

# print results
print("Year", ' ' , "Number of Fish")
for i, population in enumerate(fish_populations):
    print(i + 1, "  -  ", round(population))

print("The fish population changed by", round(abs(fish_populations[-1] - initial_fish_population)), "fish in", years, "years.")

# plot fish population over time
plt.plot(fish_populations)
plt.xlabel("Year")
plt.ylabel("Number of Fish")
plt.title("Fish Population Over Time")
plt.show()
