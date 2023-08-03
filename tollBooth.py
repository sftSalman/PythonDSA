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
        return 0.9 * TollBooth.calculate_base_toll(self)


class Car(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Car", category, weight)

    def calculate_toll(self):
        # Cars owned by government officials get a 2% discount
        if self.category == "Govt Official":
            return 0.98 * TollBooth.calculate_base_toll(self)
        else:
            return TollBooth.calculate_base_toll(self)


class Bus(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Bus", category, weight)

    def calculate_toll(self):
        return TollBooth.calculate_base_toll(self)


class Truck(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Truck", category, weight)

    def calculate_toll(self):
        return TollBooth.calculate_base_toll(self)


class Train(Vehicle):
    def __init__(self, category, weight):
        super().__init__("Train", category, weight)

    def calculate_toll(self):
        # Trains have fixed toll fees, regardless of category or weight
        return 100


class TollBooth(Vehicle):

    def calculate_base_toll(self):
        # Here, you can define your toll calculation logic based on the vehicle's type, category, and weight.
        # For simplicity, let's just use the weight of the vehicle for now.
        return 10 * self.weight


M = Motorcycle("Public", 200)
print(M.calculate_toll())
