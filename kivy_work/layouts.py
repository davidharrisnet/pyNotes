import kivy
from kivy.app import App # must be imported to provide the 'run' methoc
from kivy.uix.floatlayout import FloatLayout

class MyW(FloatLayout):
    def __init__(self, **kvargs):
        super(MyW, self).__init__(**kvargs)
        self.add_widget(MyW1())

class MyW1(FloatLayout):
    pass

class MyLayoutApp(App):  # provides the run() method
    def build(self):
        return MyW()

if __name__ == '__main__':
    MyLayoutApp().run()