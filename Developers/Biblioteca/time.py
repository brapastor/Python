__author__ = 'brapastor'

import datetime
import locale
from datetime import date
hoy = date.today()
print(hoy)
print(datetime.date(2009,7,19))

print(locale.setlocale(locale.LC_ALL,locale.getdefaultlocale()))

print(hoy.strftime("%m-%d-%y. %d %b %y es %A. hoy es %d de %B"))

# las fechas soportan aritmetica de calendario

nacimiento = date(1964, 7, 31)
edad = hoy - nacimiento
print(edad)
print(edad.days)

