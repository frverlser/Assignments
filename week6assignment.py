def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            print(f"[OK] {func.__name__} successful")
        else:
            print(f"[FAIL] {func.__name__} denied")
    return wrapper


class Equipment:
    _inventory = []
    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self._rented = 0
        Equipment._inventory.append(self)

    @log_operation
    def rent(self):
        if self._rented == self.total_units:
            return False
        else:
            self._rented += 1
            return True

    @log_operation
    def return_item(self):
        if self._rented == 0:
            return False
        else:
            self._rented -= 1
            return True

    def available(self):
        return self.total_units - self._rented

    def rental_rate(self):
        return round((self._rented / self.total_units) * 100, 1)

    @classmethod
    def from_sheet(cls, entry):
        name, units = entry.split(":")
        return cls(name, int(units))

    @staticmethod
    def is_valid_serial(serial):
        if len(serial) == 13 and "0" <= serial <= "9":
            return True
        else:
            return False

    @classmethod
    def total_available(cls):
        total = 0
        for item in cls._inventory:
            total += item.available()
        return total


e1 = Equipment("Projector", 2)
e2 = Equipment.from_sheet("Camera:3")

e1.rent()
e1.rent()
e1.rent()
e1.return_item()

e2.rent()
e2.return_item()
e2.return_item()

print(f"{e1.name}: available = {e1.available()}, rental = {e1.rental_rate()}%")
print(f"{e2.name}: available = {e2.available()}, rental = {e2.rental_rate()}%")

print(f"Valid serial '1234567890123': {Equipment.is_valid_serial('1234567890123')}")
print(f"Valid serial '123-456': {Equipment.is_valid_serial('123-456')}")
print(f"Total available in shop: {Equipment.total_available()}")
