
import iris_generator as i_gen
import feature as feats
import random

class IrisGen():

    def mutate(self, strategy):
        fts = strategy.features.copy()
        n = random.randint(len(fts))
        fts[n] = self._mutate_ft(fts[n])
        return feats.Strategy(fts)

    def _mutate_ft(self,ft):
        if ft.f_type = "float":
            if random.random
            IN HERE!!!
        




