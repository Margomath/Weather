import json
import logging
import os
import urllib.request

from mygzip import GZip

CATALOG_URL = "http://bulk.openweathermap.org/sample/city.list.json.gz"
TMP_DIR = "/tmp/"


class CityCatalog(object):
    def __init__(self, catalog_file=None):
        self.__catalog_file = None
        self.__data = None
        self.__catalog = None
        self.catalog_file = catalog_file
        self.load()

    @property
    def data(self):
        if self.__data is None:
            self.load()
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def catalog(self):
        if self.__catalog is None:
            self.parse_catalog()
        return self.__catalog

    @catalog.setter
    def catalog(self, value):
        self.__catalog = value

    @property
    def catalog_file(self):
        if self.__catalog_file is None:
            self.catalog_file = self.retrive_catalog_file()
        return self.__catalog_file

    @catalog_file.setter
    def catalog_file(self, value):
        if value is not None and os.path.isfile(value):
            self.__catalog_file = value

    @property
    def countries(self):
        return list(self.catalog.keys())

    @staticmethod
    def retrive_catalog_file():
        logging.info("Start loading catalog file...")
        filepath = TMP_DIR + "catalog.json.gz"
        urllib.request.urlretrieve(CATALOG_URL, filepath)
        extracted_path = TMP_DIR + "catalog.json"
        GZip(filepath).extract(extracted_path)
        logging.info("Finish loading catalog file...")
        return extracted_path

    def load(self):
        try:
            with open(self.catalog_file, 'r') as _file:
                self.data = json.loads(_file.read())
        except Exception as e:
            logging.error("Error reading %s: %s" % (self.catalog_file, e))

    def parse_catalog(self):
        result = {}
        for city_item in self.data:
            country = city_item["country"]
            result.setdefault(country, [])
            result[country].append({
                "id": city_item["id"],
                "name": city_item["name"]
            })
        self.catalog = result
