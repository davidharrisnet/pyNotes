from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest


class  WeatherApp(App):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=8745cdff9650c47ff8c205a2bd7ed01e"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        cities = ["{}".format(str(d))
        for d in data['weather'][0]]

        self.search_results.item_strings = cities

if __name__ == '__main__':
    WeatherApp().run()