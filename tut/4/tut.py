import kivy
from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    price = ObjectProperty(None)
    display = ObjectProperty(None)
        
    def onClick(self):
        name = self.name.text
        pizza = self.pizza.text
        price = self.price.text
        
        # print(f"Name: {name}, Pizza: {pizza}, Price: {price}")
        
        self.display.text = f"Name: {name}, Pizza: {pizza}, Price: {price}"
        
        self.name.text = ''
        self.pizza.text = ''
        self.price.text = ''

class MyApp(App):
    
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    
    app = MyApp()
    app.run()