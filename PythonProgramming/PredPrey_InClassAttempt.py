"""Scenario

Closed world (Island)
Predators (wolves) and Prey (moose)
Predators eat Prey

Island holds predators & prey

Both predators and prey can breed and move. Only predators can eat.

Simulation plays out via 'clock ticks' - scenario updates once every tick
"""


class Island:
    def __init__(self, size):
        self.grid = []
        for i in range(size):
            row = [0] * size
            self.grid.append(row)


class Animal:
    def __init__(self, x, y, breed_clock, move_clock ):
        self.x = x
        self.y = y
        self.breed_clock = breed_clock
        self.move_clock = move_clock

    def breed(self):
        pass

    def move(self):
        pass


class Predator(Animal):
    def __init__(self):
        pass


class Prey(Animal):
    pass


if __name__ == "__main__":
    main()

def main():
    GRID_SIZE = 10
    NUM_PREDATORS = 20
    NUM_PREY = 100
    PREDATOR_BREED_CLOCK = 6
    PREY_BREED_CLOCK = 3
    PREDATOR_STARVE_CLOCK = 3
    CLOCK_TICKS = 300

    my_island = Island(GRID_SIZE)

    for i in range(CLOCK_TICKS):
        pass


