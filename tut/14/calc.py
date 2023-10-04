import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)
Builder.load_file('calc.kv')

class calLayout(Widget):
    def calc_clear(self):
        self.ids.calc_display.text = '0'

class Calculator(App):
    
    def build(self):
        return calLayout()
    
if __name__ == "__main__":
    Calculator().run()