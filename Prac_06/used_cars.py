"""CP1404/CP5632 Practical - Client code to use the Car class."""

# Note that the import has a folder (module) in it.

from Prac07.car import Car

def main():

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =",limo.fuel,"\nodo =", limo.odometer)
    print(limo)

main()