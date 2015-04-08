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
    """
    Island is an n x n grid where a zero value indicates an unoccupied space.
    """
    def __init__(self, size):
        """
        Sets uo Island grid to appropriate size and fills with zeros

        :param size: size of grid
        :return: None
        """
        self.grid = []
        self.size = size
        for i in range(size):
            row = [0] * size
            self.grid.append(row)

    def __str__(self):
        """
        String representation for printing. Note that (0,0) as is customary in cartesian geometry, will be in the lower
        left position.
        """
        grid_string = ""
        for y in range(self.size-1,-1,-1):
            for x in range(self.size):
                if not self.grid[x][y]:
                    grid_string += "  .  "
                else:
                    grid_string += "  {}  ".format(str(self.grid[x][y].type))

            grid_string += "\n"
        return grid_string

    def __repr__(self):
        return self.__str__()

    def populate_island(self, predator_count, prey_count, predator_breed_clock, predator_starve_clock, prey_breed_clock,
                        move_clock):

        count = 0
        while count < predator_count:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if not self.grid[x][y]:
                self.grid[x][y] = Predator(self, x, y, breed_clock=predator_breed_clock,
                                           starve_clock=predator_starve_clock, move_clock=0)
                count += 1

        count = 0
        while count < prey_count:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if not self.grid[x][y]:
                self.grid[x][y] = Prey(self, x, y, breed_clock=prey_breed_clock, move_clock=0)
                count += 1


    def register(self, animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def clear_moved(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y]:
                    self.grid[x][y].moved = False

class Animal:
    def __init__(self, island, x, y, breed_clock=0, move_clock=0, type="A"):
        self.island = island
        self.x = x
        self.y = y
        self.breed_clock = breed_clock
        self.move_clock = move_clock
        self.type = type

        self.moved = False

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.__str__()

    def breed(self):
        pass

    def move(self):
        if not self.moved:
            x = self.x + random.randint(-1, 1)
            y = self.y + random.randint(-1, 1)

            if 0 <= x < self.island.size and 0 <= y < self.island.size:
                if not self.island.grid[x][y]:
                    self.island.grid[self.x][self.y] = 0
                    self.island.grid[x][y] = self
                    self.x = x
                    self.y = y

            self.moved = True

    def check_neighbours(self, type_wanted):
        result = None

        for i in range(8):
            x = self.x + random.randint(-1, 1)
            y = self.y + random.randint(-1, 1)

            if 0 <= x < self.island.size and 0 <= y < self.island.size:
                if type(self.island.grid[x][y] == type_wanted):
                    result = (x,y)
                    break
                else:
                    continue

        return result


class Predator(Animal):
    def __init__(self, island, x, y, breed_clock, move_clock, starve_clock, type="X"):
        Animal.__init__(self, island, x, y, breed_clock, move_clock, type)
        self.starve_clock = starve_clock


class Prey(Animal):
    def __init__(self, island, x, y, breed_clock, move_clock, type="O"):
        Animal.__init__(self, island, x, y, breed_clock, move_clock, type)


def main():
    GRID_SIZE = 10
    NUM_PREDATORS = 5
    NUM_PREY = 10
    PREDATOR_BREED_CLOCK = 6
    PREY_BREED_CLOCK = 3
    PREDATOR_STARVE_CLOCK = 3
    CLOCK_TICKS = 300

    my_island = Island(GRID_SIZE)
    my_island.populate_island(NUM_PREDATORS, NUM_PREY, PREDATOR_BREED_CLOCK, PREDATOR_STARVE_CLOCK, PREY_BREED_CLOCK, 0)

    print(my_island)

    for i in range(CLOCK_TICKS):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                animal = my_island.grid[x][y]
                if isinstance(animal, Animal):
                    animal.move()

        print(my_island)



if __name__ == "__main__":
    main()
