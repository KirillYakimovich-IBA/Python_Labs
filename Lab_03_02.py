class Vehicle:

    def __init__(self, type_of_fuel, engine_power):
        self.type_of_fuel = type_of_fuel
        self.engine_power = Engine(engine_power).engine_power
        self.message()

    def get_info(self):
        print("Тип топлива транспортного средства: " + str(self.type_of_fuel) + "; мощность двигателя: " +
              str(self.engine_power)+" л.с.")

    def message(self):
        print("Создан объект класса Vehicle.")


class Car(Vehicle):

    def __init__(self, type_of_fuel, engine_power, transmission):
        super().__init__(type_of_fuel, engine_power)
        self.transmission = transmission

    def get_info(self):
        print("Тип топлива транспортного средства: " + str(self.type_of_fuel) + "; мощность двигателя: " +
              str(self.engine_power)+" л.с.; трансмисся: "+str(self.transmission))

    def message(self):
        print("Создан объект класса Car.")


class Train(Vehicle):

    def __init__(self, type_of_fuel, engine_power, quantity_wagons):
        super().__init__(type_of_fuel, engine_power)
        self.quantity_wagons = Wagons(quantity_wagons).quantity_wagons

    def get_info(self):
        print("Тип топлива транспортного средства: " + str(self.type_of_fuel) + "; мощность двигателя: " +
              str(self.engine_power) + " л.с.; количество вагонов: " + str(self.quantity_wagons))

    def message(self):
        print("Создан объект класса Train.")


class Express(Train):
    max_speed = 400

    def __init__(self, type_of_fuel, engine_power, quantity_wagons):
        super().__init__(type_of_fuel, engine_power, quantity_wagons)

    def get_info(self):
        print("Тип топлива транспортного средства: " + str(self.type_of_fuel) + "; мощность двигателя: " +
              str(self.engine_power) + " л.с.; количество вагонов: " + str(self.quantity_wagons) + "; максимальная скорость: " +
              str(self.max_speed))

    def message(self):
        print("Создан объект класса Express")


class Engine:
    engine_power = ''

    def __init__(self, engine_power):
        self.engine_power = engine_power


class Wagons:
    quantity_wagons = 0

    def __init__(self, quantity_wagons):
        self.quantity_wagons = quantity_wagons


vehicle_01 = Car('бензин', 200, 'МКПП')
vehicle_01.get_info()
vehicle_02 = Train('дизель', 800, '15')
vehicle_02.get_info()
vehicle_03 = Express('электро', 1000, 5)
vehicle_03.get_info()

