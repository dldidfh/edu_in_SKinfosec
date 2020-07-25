
class ProEntity:
    def __init__(self, proName,proPrice,proWeight,proSize):
        self.proName = proName
        self.proPrice = proPrice
        self.proWeight = proWeight
        self.proSize = proSize

    def __eq__(self,proName):
        if(self.proName == proName):
            return True
        else:
            return False

