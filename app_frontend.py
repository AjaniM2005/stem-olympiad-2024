from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        
        self.orientation = 'vertical'
        self.add_widget(Label(text="Welcome to the Geohazards App!", font_size=30))

        
        nav_menu = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        nav_menu.add_widget(Button(text="Home", on_press=self.go_home))
        nav_menu.add_widget(Button(text="Prediction", on_press=self.go_prediction))
        nav_menu.add_widget(Button(text="Preparedness", on_press=self.go_preparedness))
        nav_menu.add_widget(Button(text="Learn", on_press=self.go_learn))

        self.add_widget(nav_menu)

    def go_home(self, instance):
        print("Navigate to Home")

    def go_prediction(self, instance):
        print("Navigate to Prediction")

    def go_preparedness(self, instance):
        print("Navigate to Preparedness")

    def go_learn(self, instance):
        print("Navigate to Learn")

class GeohazardsApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    GeohazardsApp().run()
class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.add_widget(Label(text="Welcome to the Geohazards App!", font_size=30))


        nav_menu = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        nav_menu.add_widget(Image(source='home_icon.png', size_hint=(None, None), size=(50, 50), on_press=self.go_home))
        nav_menu.add_widget(Image(source='prediction_icon.png', size_hint=(None, None), size=(50, 50), on_press=self.go_prediction))
        nav_menu.add_widget(Image(source='preparedness_icon.png', size_hint=(None, None), size=(50, 50), on_press=self.go_preparedness))
        nav_menu.add_widget(Image(source='learn_icon.png', size_hint=(None, None), size=(50, 50), on_press=self.go_learn))

        self.add_widget(nav_menu)
       