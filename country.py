

class Country(object):
    def __init__(self, cities_catalog):
        self.__catalog = cities_catalog
        self.__country_name = None
        self.__cities = None

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, value):
        if value in self.__catalog.catalog:
            self.__country_name = value
            self.__cities = sorted([(x["id"], x["name"]) for x in self.__catalog.catalog[value]])

    @property
    def cities(self):
        return self.__cities
