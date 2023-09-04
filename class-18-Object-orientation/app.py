# Inporting the car class

from car import Car

beetle = Car("Volks", "Beetle", "Black", "Gasoline")

beetle.turn_on()
beetle.turn_on()

for index in range(100):
    beetle.speed_up()

for i in range(60):
    beetle.brake()

beetle.turn_off()

porche = Car("Porche", "Porche Carrera 911", "Silver", "Gasoline")

porche.turn_on()
for i in range(300):
    porche.speed_up()
for i in range(299):
    porche.brake()
porche.turn_off()
