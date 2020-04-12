from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, Label

from cities import CityCatalog
from country import Country
from recommendations import Recommendations
from weather import Weather

app = Flask(__name__, template_folder='templates')

city_catalog = CityCatalog(catalog_file="city.list.json")
country_choices = sorted([(country, country) for country in city_catalog.countries if len(country) > 0])
country = Country(city_catalog)


def city_choises(country_name):
    country.country_name = country_name
    return country.cities


class InputForm(FlaskForm):
    country = SelectField('Country', choices=country_choices)
    submit_country = SubmitField('Submit country')
    city = SelectField('City', choices=[])
    submit_city = SubmitField('Submit city')


class WeatherForm(FlaskForm):
    city = Label(0, "")
    temperature = Label(1, "")
    humidity = Label(2, "")
    pressure = Label(3, "")
    wind_speed = Label(4, "")
    weather_desc = Label(5, "")
    recommendations = Label(6, "")
    back_btn = SubmitField('Назад')


def get_weather(city_id):
    weather = Weather()
    weather.city_id = city_id
    return weather


def render_weather(weather, rec):
    name = None
    form = WeatherForm()
    city_tpl = "Город: %s"
    temperature_tpl = "Температура: %s C"
    humidity_tpl = "Влажность: %s процентов"
    pressure_tpl = "Давление: %s кПа"
    wind_speed_tpl = "Скорость ветра: %s м/с"
    weather_desc_tpl = "Описание: %s"
    recommendations_tpl = "Рекомендуем надеть: %s"

    form.city.text = city_tpl % weather.city
    form.temperature.text = temperature_tpl % weather.temperature
    form.humidity.text = humidity_tpl % weather.humidity
    form.pressure.text = pressure_tpl % weather.pressure
    form.wind_speed.text = wind_speed_tpl % weather.wind_speed
    form.weather_desc.text = weather_desc_tpl % weather.weather_desc
    clothes, accessories = rec.recommendation
    form.recommendations.text = recommendations_tpl % clothes
    if len(accessories) > 0:
        form.recommendations.text += "<br/>Не забудьте захватить: " + accessories
    return render_template('result.html', form=form, name=name)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = InputForm()
    country_name = form.country.data
    city = form.city.data
    if form.data["submit_country"] and country_name is not None:
        form.city.choices = city_choises(country_name)
    if form.data["submit_city"] and city != "None":
        weather = get_weather(city)
        rec = Recommendations(weather)
        return render_weather(weather, rec)
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    app.run(host="127.0.0.1", port=8080)
