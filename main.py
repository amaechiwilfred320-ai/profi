from kivy.app import App
from kivy.uix.label import Label

class ProfiApp(App):
    def build(self):
        return Label(text="Hello, this is Profi - Best App!")

if __name__ == "__main__":
    ProfiApp().run()
