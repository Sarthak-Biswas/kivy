import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder

Builder.load_file('update_label.kv')

class MyLayout(Widget):
    
    def press(self):
        name = self.ids.name_input.text
        
        self.ids.name_display.text = f"Hello {name} !!!"
        
        self.ids.name_input.text = ''

class MyApp(App):
    
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    MyApp().run()