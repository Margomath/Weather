

class Recommendations(object):
    def __init__(self, weather):
        self.weather = weather

    @property
    def recommendation(self):
        clothes = []
        accessories = []
        if self.weather.is_rain:
            clothes.append("резиновые сапоги")
            if self.weather.wind_speed > 8:
                clothes.append("дождевик")
            else:
                accessories.append("зонт")
            if self.weather.temperature > 7:
                if self.weather.temperature > 25:
                    clothes.append("шорты")
                    clothes.append("футболку")
                else:
                    clothes.append("толстовку")
                    clothes.append("джинсы")
            else:
                accessories.append("перчатки")
                clothes.append("куртку")
                clothes.append("джинсы")
        else:
            if self.weather.temperature > 0:
                if self.weather.temperature > 25:
                    clothes.append("шорты")
                    clothes.append("футболку")
                    clothes.append("сандали")
                    if self.weather.main_id == 800 or self.weather.main_id == 801:
                        accessories.append("очки")
                        accessories.append("бейсболку")
                else:
                    if self.weather.temperature > 5:
                        clothes.append("толстовку")
                        clothes.append("джинсы")
                        clothes.append("кроссовки")
                    else:
                        accessories.append("перчатки")
                        clothes.append("куртку")
                        clothes.append("джинсы")
                        clothes.append("ботинки")
            else:
                clothes.append("шапку")
                clothes.append("шарф")

                if self.weather.temperature < - 5:
                    clothes.append("зимние ботинки")
                    accessories.append("рукавицы")
                    clothes.append("тёплые штаны")
                    if self.weather.temperature < -18:
                        clothes.append("термобельё")
                        clothes.append("шерстяные носки")
                        clothes.append("дублёнку")
                    else:
                        clothes.append("пуховик")
                else:
                    clothes.append("перчатки")
                    clothes.append("куртку")
                    clothes.append("джинсы")
                    clothes.append("ботинки")
        return ", ".join(clothes), ", ".join(accessories)
