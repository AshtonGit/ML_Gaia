class genomeManager(object):

    def __init__(self):
        self.species = {}
        self.genomes = {}
        return

    def initialisePool(self):
        return

    # Population management

    def cullSpecies(species):
        return

    # remove species that are "stuck" at local maxima/minima
    def removeStaleSpecies(self):
        return

    # Remove all members of the weakest species
    def removeWeakSpecies(self):
        return

    # Fitness
    def calcAverageFitness(self, species):
        return

    def totalAverageFitness(self):
        return

    def rankGlobally(self):
        return

    # Species categorisation / management
    def addToSpecies(self, child):
        return

    # writes all genomes in ecology to a file
    def saveEcologyToFile(self, filename):
        return

    def onExit(self):
        return
