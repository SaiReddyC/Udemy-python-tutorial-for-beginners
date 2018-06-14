from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country("India", 1200, 100),
             Country("China", 1400, 200),
             Country("USA", 1200, 100)]


countries.append(Country("Russia", 80, 900))
print(countries)

countries.sort(key=attrgetter("population"), reverse=True)
print(countries)
