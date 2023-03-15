import neat as nt


class Organism(object):

    def __init__(self):
        self.model = None
        return

    def getResource(self):
        return

    def getInputs(self):
        return

    def reproduceClone(self):
        return

    def reproduceBreed(self):
        return

    def crossover(self, gene1, gene2):
        return

    # Single Genes
    def newGene(self):
        return

    def copyGene(self, gene):
        return

    # Genomes
    def newGenome(self):
        genome = {}
        return genome

    def copyGenome(self, genome):
        return

    # Neurons
    def newNeuron(self):
        return

    def randomNeuron(self, genes, nonInput):
        return

    # Networks
    def newNetwork(self):
        model = nt.nn.FeedForwardNetwork()
        return model

    def evaluateNetwork(network, inputs):
        return

    # Mutation and Network Management

    def mutate(self, genome):
        return

    def containsLink(self, genes, link):
        return

    def pointMutate(self, genome):
        return

    def linkMutate(self, genome, forceBias):
        return

    def nodeMutate(self, genome):
        return

    # enable / disable mutation for a given genome
    def toggleMutate(self, genome, enable):
        return

    def disjoint(self, genes1, genes2):
        return

    # Are two genomes the same species?
    def sameSpecies(self, genome1, genome2):
        return
