import paho.mqtt.publish as publish
from colorama import Fore

print(f"Приклад Локації:\n{Fore.YELLOW}Портер Паб:\n 50.43047429254061, 30.473396375767976")
print(f"{Fore.YELLOW}Будівельний Університет:\n 50.426695583914906, 30.46562531363436")
print(Fore.WHITE + "Введіть Ваше Місцезнаходження:")
loc = input()

publish.single("userloc", loc, hostname="localhost")




