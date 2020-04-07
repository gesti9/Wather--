from colorama import init
from colorama import Fore, Back, Style

import pyowm
init()

print(Fore.BLACK )
print(Back.CYAN )
owm = pyowm.OWM('7c9f41e4faf7b9046a78088c174938b8', language = "ru" )

place = input("Какой город тебя интересует?: ")
def check_city(place):
	try:
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]
		print(Back.YELLOW)
		print("В городе " + place + " сейчас " + w.get_detailed_status())
		print(Back.RED)
		print("Температура сейчас в районе " + str(temp) + "градусов" )
	except pyowm.exceptions.api_response_error.NotFoundError:
		print("Вы ввели не правильный город ")
		if temp < 10:
			print("Одевайся тепло!!!!!")
		elif temp < 20:
			print("Нормально одевайся!!")
		else:
			print("Погода норм")

input()