import requests

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s"
API_KEY = "d1cd5b80a05926b9636d0728154e1880"


class Weather(object):
    def __init__(self):
        self.city_id = None
        self.__weather = None

    @property
    def weather(self):
        if self.__weather is None:
            self.get_weather()
        return self.__weather

    @weather.setter
    def weather(self, value):
        self.__weather = value

    def check(self):
        if self.weather is None:
            self.get_weather()

    @property
    def temperature(self):
        temp = self.weather.get("main", {}).get("temp")
        return int(temp - 273.15)

    @property
    def humidity(self):
        return self.weather.get("main", {}).get("humidity")

    @property
    def pressure(self):
        if self.weather is None:
            self.get_weather()
        if isinstance(self.weather, dict):
            return self.weather.get("main", {}).get("pressure")

    @property
    def wind_speed(self):
        return self.weather.get("wind", {}).get("speed")

    @property
    def city(self):
        return self.weather.get("name", "")

    @property
    def weather_desc(self):
        weather = self.weather.get("weather", [])
        if len(weather) > 0 and isinstance(weather[0], dict):
            return "%s: %s" % (weather[0]["main"], weather[0]["description"])

    @property
    def main_id(self):
        weather = self.weather.get("weather", [])
        if len(weather) > 0 and isinstance(weather[0], dict):
            return weather[0]["id"]

    @property
    def is_rain(self):
        weather = self.weather.get("weather", [])
        if len(weather) > 0 and isinstance(weather[0], dict):
            return str(weather[0]["id"]).startswith("5")

    def get_weather(self):
        url = WEATHER_URL % (self.city_id, API_KEY)
        self.weather = requests.get(url).json()
