from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class whateverApp(App):

	def build(self):

		def gettheloops():
			mes_volt = float(textinput.text)
			measured_loops = round((mes_volt / 33), 4)

			return str(measured_loops)

		def on_enter(instance):
			textoutput.text = 'ive typed in ' + gettheloops()

		def on_text(instance, value):
			textoutput.text = 'ive typed in ' + gettheloops()

		textinput = TextInput(text = ' ', multiline=False)
		textinput.bind(on_text_validate=on_enter)
		textinput.bind(text=on_text)

		textoutput = Label(text = 'TRIOL inc.')

		united_layout = BoxLayout(orientation = 'vertical')
		united_layout.add_widget(textinput)
		united_layout.add_widget(textoutput)

		return united_layout

if __name__ == '__main__':
	whateverApp().run()