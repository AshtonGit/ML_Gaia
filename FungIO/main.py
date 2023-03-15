import neat

from organisms import Organism
from neat import config as conf

config = conf.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     "./venv/config")
pop = neat.population.Population(config)
