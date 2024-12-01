from ast import And
import random
import string
import colorama
from colorama import Fore
import time
colorama.init()
length = 50
h = '*************************'
captcha = print ('[🤖]     ' + Fore.YELLOW + "Captcha detected")
xal = print ('[✅]      ' + Fore.LIGHTMAGENTA_EX + "XAL has been solved")
hcaptcha = print ("[🟩]     " + Fore.LIGHTGREEN_EX + "Hcaptcha has been solved")
register = print ("[✉️]     " + Fore.LIGHTBLUE_EX + "Epic games has been registered")
email = print ('[💌]        ' + Fore.CYAN + "Email has been verified")
rnd = ''.join(random.choices(string.ascii_lowercase, k=length))
promo = print ('[🌐]        ' +  Fore.BLUE + "Promo has been pulled:https://discord.com/billing/partner-promotions/" + rnd + h) 
a = 0
while a == a:
    num = random.randint(0,6)
    if num == 1:
        time.sleep (0.3)
        captcha = print ('[🤖]     ' + Fore.YELLOW + "Captcha detected")
        print (captcha)
    if num == 2:
        time.sleep (0.1)
        xal = print ('[✅]      ' + Fore.LIGHTMAGENTA_EX + "XAL has been solved")
        print (xal)
    if num == 3:
        time.sleep (0.05)
        hcaptcha = print ("[🟩]     " + Fore.LIGHTGREEN_EX + "Hcaptcha has been solved")
        print (hcaptcha)
    if num == 4:
        time.sleep (0.2)
        register = print ("[✉️]     " + Fore.LIGHTBLUE_EX + "Epic games has been registered")
        print (register)
    if num == 5:
        time.sleep (0.25)
        email = print ('[💌]        ' + Fore.CYAN + "Email has been verified")
        print (email)
    else:
        time.sleep (0.4)
        rnd = ''.join(random.choices(string.ascii_lowercase, k=length))
        promo = print ('[🌐]        ' +  Fore.BLUE + "Promo has been pulled:https://discord.com/billing/partner-promotions/" + rnd + h) 
        print (promo)