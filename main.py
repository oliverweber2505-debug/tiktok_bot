from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests

class TikTokBotApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = Label(text="TikTok Bot ist bereit", font_size='20sp')
        layout.add_widget(self.label)
        
        btn = Button(text="Bot starten", size_hint=(1, 0.3))
        btn.bind(on_press=self.run_bot)
        layout.add_widget(btn)
        
        return layout

    def run_bot(self, instance):
        self.label.text = "Bot läuft..."
        # Hier kommt deine Bot-Logik rein (z.B. Requests an APIs)
        try:
            response = requests.get("https://api.github.com")
            if response.status_code == 200:
                self.label.text = "Verbindung erfolgreich!"
            else:
                self.label.text = "Fehler bei Verbindung."
        except Exception as e:
            self.label.text = f"Fehler: {str(e)}"

if __name__ == '__main__':
    TikTokBotApp().run()
