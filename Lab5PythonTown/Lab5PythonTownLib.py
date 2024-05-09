class Town:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.region = ""
        self.population = 0
        self.year_income = 0.0
        self.square = 0.0
        self.has_port = False
        self.has_airport = False

    @property
    def year_income_per_inhabitant(self):
        if self.population > 0:
            return self.year_income / self.population
        else:
            return 0