import random


class GenProgStrategy:

    def __init__(self, sample_size, tourn_size, p_cross, p_mut, p_elite, n_generations):

        self._sample_size = sample_size

        self._tourn_size = tourn_size

        self._p_cross = p_cross

        self._p_mut = p_mut

        self._p_elite = p_elite

        self._n_generations = n_generations

    def evolve(self, generator, mutator, crosser, decider):
        """
        Uses genetic programming to evolve an improved version of a gene
        :param generator: Generator that provides random genes for use in an original sample
        :param mutator: Mutator that can mutate a gene
        :param crosser: Object that can apply crossover to two genes
        :param decider: Object that can determine the best gene given a list
        :return: An evolved gene
        """
        if self._p_cross + self._p_elite + self._p_mut > 1:
            raise ArithmeticError("Proportions of cross over, elitism and mutation add to more than 1")

        # Calculate number to select for crossover, mutation and elitism for each generation
        n_cross = int(self._sample_size * self._p_cross)
        n_mut = int(self._sample_size * self._p_mut)
        n_elite = int(self._sample_size + self._p_elite)
        n_select = self._sample_size - n_cross - n_mut - n_elite

        sample = [generator.random_gene() for _ in range(self._sample_size)]

        n = self._n_generations

        while n > 0:

            new_mutated = [mutator.mutate(self._select_gene(sample, decider)) for n in range(n_mut)]
            new_co = [crosser.crossover(self._select_gene(sample, decider), self._select_gene(sample, decider)) for n
                      in range(n_cross)]
            new_elite = decider.best_n(sample, n_elite)
            new_selected = [self._select_gene(sample, decider) for _ in range(n_select)]

            sample = new_mutated + new_co + new_elite + new_selected

            n = n-1

        return sample

    def _select_gene(self,sample,decider):
        return decider.best_n(random.sample(sample, self._tourn_size), 1)
