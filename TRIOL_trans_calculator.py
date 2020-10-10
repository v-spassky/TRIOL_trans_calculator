# Мобильное приложения для испытателя обмоток трансформатора
# На основании измерения напряжения между концами обмотки приложение должно выдавать колчество витков между этими концами

# Импорт
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# Настраиваю размер окна
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '270');
Config.set('graphics', 'height', '585');


class calculusApp(App):

	def build(self):

		def gettheloops():

			measured_loops = ''

			if (powerinput_btn.text == ' ') or (controlvoltage_btn.text == ' ') or (measuredvoltage_btn.text == ' '):
				measured_loops = 111

			if (powerinput_btn.text != ' ') and (controlvoltage_btn.text != ' ') and (measuredvoltage_btn.text != ' ') and (powerinput_btn.text != '') and (controlvoltage_btn.text != '') and (measuredvoltage_btn.text != ''):
				prim_power = float(powerinput_btn.text)
				ctrl_volt = float(controlvoltage_btn.text)
				mes_volt = float(measuredvoltage_btn.text)

				if (prim_power == 0) or (ctrl_volt == 0) or (mes_volt == 0):
					measured_loops = 111

				loop_per_volt = ctrl_volt / 150
				measured_loops = round(mes_volt / loop_per_volt, 4)

			return str(measured_loops)

		def on_enter(instance):
			fin_label.text = 'The calculated number\n of loops is: ' + gettheloops()
		
		def on_text(instance, value):
			fin_label.text = 'The calculated number\n of loops is: ' + gettheloops()

		# задаю общий лейаут
		united_layout = BoxLayout(orientation = 'vertical')

		# включаю в общий лейаут три лейаута, отображающих три графические области (top, side, bot)
		toppart_layout = BoxLayout(orientation = 'vertical', size_hint = (1, .2))
		united_layout.add_widget(toppart_layout)

		sidepart_layout = BoxLayout(orientation = 'vertical', size_hint = (1, .6))
		united_layout.add_widget(sidepart_layout)

		botpart_layout = BoxLayout(orientation = 'horizontal', size_hint = (1, .2))
		united_layout.add_widget(botpart_layout)


		# наполнение графических областей
		# в верхней области только информация
		toppart_layout.add_widget(Label(text = 'TRIOL inc.'))
		toppart_layout.add_widget(Label(font_size = 14, text = 'This calculator returns a number of\n loops in a single coil. Put all\n the necessary measured data in the\n input windows below and obtain the\n number at the bottom of the window.'))

		# в средней области окна ввода текста, и подписи над каждым окном
		# первое окно и подпись
		sidepart_layout.add_widget(Label(halign = 'left', valign = 'bottom',text = 'Power on the primary coli (Wt):', size_hint = (.8, .125)))
		powerinput_btn = TextInput(text = ' ', size_hint = (1, .125), multiline=False)
		sidepart_layout.add_widget(powerinput_btn)
		powerinput_btn.bind(on_text_validate=on_enter)
		powerinput_btn.bind(text=on_text)

		# второе окно и подпись
		sidepart_layout.add_widget(Label(halign = 'left', text = 'Voltage on the control coil (V):', size_hint = (.8, .125)))
		controlvoltage_btn = TextInput(text = ' ', size_hint = (1, .125), multiline=False)
		sidepart_layout.add_widget(controlvoltage_btn)
		controlvoltage_btn.bind(on_text_validate=on_enter)
		controlvoltage_btn.bind(text=on_text)

		# третье окно и подпись
		sidepart_layout.add_widget(Label(halign = 'left', text = 'Voltage on the measured coil (V):', size_hint = (.85, .125)))
		measuredvoltage_btn = TextInput(text = ' ', size_hint = (1, .125), multiline=False)
		sidepart_layout.add_widget(measuredvoltage_btn)
		measuredvoltage_btn.bind(on_text_validate=on_enter)
		measuredvoltage_btn.bind(text=on_text)

		fin_label = Label(font_size = 20, text = 'The calculated number\n of loops is: ')
		botpart_layout.add_widget(fin_label)


		return united_layout

if __name__ == '__main__':
	calculusApp().run()