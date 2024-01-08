# app_frontend.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder

# Load the Kivy language file
Builder.load_file("kivy/kivy_app.kv")

class MainScreen(BoxLayout):
    pass

class GeohazardApp(App):
    def build(self):
        return MainScreen()

    def load_data(self):
        # Implement logic to load data
        # For now, display a placeholder message
        self.show_popup('Data Loaded', 'Placeholder message for data loading.')

    def visualize_data(self):
        # Implement logic to visualize data
        # For now, display a placeholder message
        self.show_popup('Data Visualization', 'Placeholder message for data visualization.')

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    GeohazardApp().run()
