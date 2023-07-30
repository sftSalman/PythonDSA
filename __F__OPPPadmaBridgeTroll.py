class Vehicle:
    def __init__(self, vehicle_type, category, weight):
        self.vehicle_type = vehicle_type
        self.category = category
        self.weight = weight

    def calculate_toll(self):
        # Default toll calculation for unknown vehicle types
        return 0


class Motorcycle(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Motorcycle", category, weight)

    def calculate_toll(self):
        # Motorcycles get a 10% discount for all categories
        return 0.9 * self.calculate_base_toll()


class Car(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Car", category, weight)

    def calculate_toll(self):
        # Cars owned by government officials get a 2% discount
        if self.category == "Govt Official":
            return 0.98 * self.calculate_base_toll()
        else:
            return self.calculate_base_toll()


class Bus(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Bus", category, weight)

    def calculate_toll(self):
        return self.calculate_base_toll()


class Truck(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Truck", category, weight)

    def calculate_toll(self):
        return self.


class Train(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Train", category, weight)

    def calculate_toll(self):
        # Trains have fixed toll fees, regardless of category or weight
        return 100






v1 = Truck('Truck',1000)
print(v1.calculate_toll())