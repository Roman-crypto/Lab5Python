class Country:
    def __init__(self):
        self.Name = ""
        self.Capital = ""
        self.Population = 0
        self.Area = 0.0
        self.Language = ""
        self.IsUNMember = False
        self.DevelopmentLevel = ""
    
    @property
    def PopulationDensity(self):
        return self.GetPopulationDensity()
    
    def GetPopulationDensity(self):
        return self.Population / self.Area