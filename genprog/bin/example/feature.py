

"""
An example class that can be used to generate a feature 
"""
class Feature:

    def __init__(self, left,right,comps,f_type=None):
        self.left = left
        self.right = right
        self.comps = comps
        self.f_type = f_type

class Strategy:
    
    def __init__(self,features):
        self.features = features
        self.depth = len(features)


    