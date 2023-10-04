import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.input_grid = GridLayout()
        self.input_grid.cols = 2
        
        self.label1 = Label(text='Name: ', font_size=40)
        self.input_grid.add_widget(self.label1)
        
        self.name = TextInput(multiline=False)
        self.input_grid.add_widget(self.name)
        
        self.label2 = Label(text='Pizza: ', font_size=40)
        self.input_grid.add_widget(self.label2)
        
        self.pizza = TextInput(multiline=False)
        self.input_grid.add_widget(self.pizza)
        
        self.label3 = Label(text='Price: ', font_size=40)
        self.input_grid.add_widget(self.label3)
        
        self.price = TextInput(multiline=False)
        self.input_grid.add_widget(self.price)
        
        self.add_widget(self.input_grid)
        
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press = self.onClick)
        self.add_widget(self.submit)
        
        self.display = Label(text='')
        self.add_widget(self.display)
        
    def onClick(self, instance):
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