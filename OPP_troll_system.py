class Vehicle:
    def __init__(self, vehicle_type, category, weight):
        self.vehicle_type = vehicle_type
        self.category = category
        self.weight = weight

    def calculate_toll(self):
        return 0


class Motorcycle(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Motorcycle", category, weight)

    def calculate_toll(self):
        return 10


class Car(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Car", category, weight)

    def calculate_toll(self):
        if self.category == "Govt Official":
            return 0
        return 100


class Bus(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Bus", category, weight)

    def calculate_toll(self):
        return 200


class Truck(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Truck", category, weight)

    def calculate_toll(self):
        return 300


class Train(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Train", category, weight)

    def calculate_toll(self):
        return 500


class PlatinumCardHolder:
    def __init__(self):
        self.discount = 0.1


class GoldCardHolder:
    def __init__(self):
        self.discount = 0.08


class SilverCardHolder:
    def __init__(self):
        self.discount = 0.05


def calculate_toll(vehicle):
    toll_amount = vehicle.calculate_toll()

    if isinstance(vehicle.category, PlatinumCardHolder):
        toll_amount -= toll_amount * vehicle.category.discount
    elif isinstance(vehicle.category, GoldCardHolder):
        toll_amount -= toll_amount * vehicle.category.discount
    elif isinstance(vehicle.category, SilverCardHolder):
        toll_amount -= toll_amount * vehicle.category.discount

    return toll_amount


# Example usage
motorcycle = Motorcycle("Public", 100)
car = Car("Personal", 1500)
bus = Bus("Govt Official", 5000)
truck = Truck("Carriage of Goods", 10000)
train = Train("Public", 50000)

platinum_card = PlatinumCardHolder()
gold_card = GoldCardHolder()
silver_card = SilverCardHolder()

car.category = platinum_card
bus.category = gold_card
truck.category = silver_card

print("Toll for Motorcycle:", calculate_toll(motorcycle))
print("Toll for Car:", calculate_toll(car))
print("Toll for Bus:", calculate_toll(bus))
print("Toll for Truck:", calculate_toll(truck))
print("Toll for Train:", calculate_toll(train))
