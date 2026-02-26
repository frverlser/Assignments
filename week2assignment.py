class BikeStation:
    def __init__(self, name, total_docks, rented_bikes=0):
        self._name = name
        self.total_docks = total_docks 
        self.rented_bikes = rented_bikes 
    @property
    def name(self):
        return self._name

    @property
    def total_docks(self):
        return self._total_docks

    @total_docks.setter
    def total_docks(self, value):
        if value < 1:
            raise ValueError("Total docks must be at least 1")
        self._total_docks = value 
    @property
    def rented_bikes(self):
        return self._rented_bikes

    @rented_bikes.setter
    def rented_bikes(self, value):
        if value < 0:
            raise ValueError("Rented bikes cannot be negative")
        if value > self.total_docks:
            raise ValueError("Rented bikes cannot exceed total docks")
        self._rented_bikes = value 
    @property
    def available_bikes(self):
        return self.total_docks - self.rented_bikes

    @property
    def rental_rate(self):
        return f"{((self.rented_bikes / self.total_docks) * 100):.1f}"

    def rent(self, value):
        if value <= 0:
            raise ValueError("Number of bikes must be positive")
        if value > self.available_bikes: 
            raise ValueError("Not enough available bikes")
        self.rented_bikes += value 

    def dock(self, value):
        if value <= 0:
            raise ValueError("Number of bikes must be positive")
        if value > self.rented_bikes:
            raise ValueError("Cannot dock more than rented")
        self.rented_bikes -= value 

s = BikeStation("Central Park", 25)
print(s.name, s.available_bikes, s.rental_rate)

s.rent(15)
print(s.rented_bikes, s.rental_rate)

s.dock(5)
print(s.available_bikes)

try:
    s.rent(20)
except ValueError as e:
    print(e)

try:
    s.name = "X"
except AttributeError:
    print("Cannot change station name")