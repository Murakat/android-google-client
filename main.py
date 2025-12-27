from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
import webbrowser

class GoogleClientApp(App):
    def build(self):
        self.store = JsonStore('settings.json')
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="Google Client", font_size='24sp', size_hint=(1, 0.2))
        self.layout.add_widget(self.label)

        self.btn_login = Button(text="ВОЙТИ (LOGIN)", font_size='20sp', background_color=(0, 0.6, 0, 1))
        self.btn_login.bind(on_press=self.open_google)
        self.layout.add_widget(self.btn_login)

        self.btn_settings = Button(text="Настройки IP / DNS", font_size='16sp', size_hint=(1, 0.3))
        self.btn_settings.bind(on_press=self.open_settings)
        self.layout.add_widget(self.btn_settings)
        return self.layout

    def open_google(self, instance):
        if self.store.exists('dns'):
            custom_ip = self.store.get('dns')['ip']
        else:
            custom_ip = "172.217.16.142"

        base_url = "https://" + custom_ip + "/ServiceLogin"
        self.label.text = "Запускаю..."
        webbrowser.open(base_url)

    def open_settings(self, instance):
        content = BoxLayout(orientation='vertical', padding=10)
        lbl = Label(text="Введите IP адрес:")
        content.add_widget(lbl)
        
        saved_ip = "172.217.16.142"
        if self.store.exists('dns'):
            saved_ip = self.store.get('dns')['ip']
        
        text_input = TextInput(text=saved_ip, multiline=False)
        content.add_widget(text_input)
        
        save_btn = Button(text="СОХРАНИТЬ", size_hint=(1, 0.5))
        content.add_widget(save_btn)
        popup = Popup(title='Настройки', content=content, size_hint=(0.9, 0.5))
        
        def save(btn):
            self.store.put('dns', ip=text_input.text, enabled=True)
            popup.dismiss()
        save_btn.bind(on_press=save)
        popup.open()

if __name__ == '__main__':
    GoogleClientApp().run()