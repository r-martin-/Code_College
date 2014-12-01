"""
Predator-Prey Problem
---------------------
Simulation of natural habitat
* 2 groups of animals interact
* Prey = food source for predators
* Both populations struggle to survive
* Both groups have fixed birthrate – prey usually faster than predators
allowing for growing prey population
* Increasing prey => habitat can support a greater predator population
=> reducing prey over time
* Both populations in cycle of growth & decay
* We get to choose what is represented so simulation is much simplified.
We can adjust birth & death rates and see what happens
* Example based on wolves & moose on island in Lake Superior.
The island is isolated thus represents a fairly closed world

Rules
    1. Habitat updates itself in units of time called clock ticks. During
    tick each animal gets to do something
    2. All animals have opportunity to move into adjacent space if
    available. One move p/tick allowed.
    3. Both predator & prey can reproduce. Each animal is assigned a
    fixed breed time. If the animal is still alive after breed-time
    clock ticks it will reproduce. It does so by finding an unoccupied
    adjacent space. The offspring is created in this space. The animal's
    breed-time is reset to zero. Can breed at most once p/tick.
    4. Predators must eat. They have a fixed starve-time. If they cannot
    find prey within starve-time clock ticks, they die.
    5. Eats by moving to adjacent space containing predator.
    Starve-time reset to zero. Eating counts as a move.
    6. Each animal's local state updated after each tick.

Simulation using OO Programming
Identify objects and their interactions. Objects that we need:
    An island
    some prey (the moose)
    some predators (the wolves)
    methods that govern how they interact with each other and the main
    program.
"""

import random

class Island:
    def __init__(self, size):
        self.size = size
        self.grid = []

        for i in range(size):
            row = [0]*size
            self.grid.append(row)

    def __str__(self):
        grid_string = ""

        for x in range(self.size):
            for y in range(self.size):
                if not self.grid[x][y]:
                    grid_string += "  .  "
                else:
                    grid_string += "  {}  ".format(str(self.grid[x][y]))
            grid_string += "\n"

        return grid_string

    def populate(self, num_predators, num_prey):

        count = 0
        while count < num_predators:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            if not self.grid[x][y]:
                self.grid[x][y] = Predator(x,y)
                count += 1

class Animal:
    def __init__(self, x, y, breed_time=0, type="A"):
        self.x = x
        self.y = y
        self.breed_time = breed_time
        self.type = type

    def __str__(self):
        return "{}".format(self.type)


class Predator(Animal):
    def __init__(self, x, y, breed_time=0, type="X", starve_time=0):
        Animal.__init__(self, x, y, breed_time, type)
        self.starve_time = starve_time



class Prey(Animal):
    pass

def main():
    GRID_SIZE = 10
    NUM_PREDATORS = 1
    NUM_PREY = 100
    PREDATOR_BREED_CLOCK = 6
    PREY_BREED_CLOCK = 3
    PREDATOR_STARVE_CLOCK = 3
    CLOCK_TICKS = 300

    my_island = Island(GRID_SIZE)
    print(my_island)

    my_island.populate(NUM_PREDATORS, NUM_PREY)

    print(my_island)

    # my_wolf = Predator(2, 3, 6, "X", 3)
    # print(my_wolf)
    #
    # my_moose = Prey(4, 6, 6, "O")
    # print(my_moose)

    print(my_island)

if __name__ == "__main__":
    main()
