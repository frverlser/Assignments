class Prescription:
    def __init__(self, medication_name=str, price_per_pill=float, pill_count=int):
        self.medication_name = medication_name
        self.price_per_pill = price_per_pill
        self.pill_count = pill_count
    def __str__(self):
        return (f"{self.medication_name}: {self.pill_count} pill(s) at ${self.price_per_pill}")
    def __repr__(self):
        return f"Prescription('{self.medication_name}', {self.price_per_pill}, {self.pill_count})"
    def __add__(self, value):
        if isinstance(value, Prescription):
            if self.medication_name == value.medication_name:
                total_pills = self.pill_count + value.pill_count
                return Prescription(self.medication_name, self.price_per_pill, total_pills)
            else:
                return NotImplemented
        elif isinstance(value, int):
            return f"{self.medication_name}: {self.pill_count + value} pill(s) at ${self.price_per_pill}"
        else:
            NotImplemented
    def __eq__(self, value):
        if isinstance(value, Prescription):
            return (self.medication_name, self.price_per_pill) == (value.medication_name, value.price_per_pill)
        return NotImplemented
    def __bool__(self):
        return self.pill_count > 0
script1 = Prescription("Amoxicillin", 1.2, 30)
script2 = Prescription("Amoxicillin", 1.2, 15)
script3 = Prescription("Ibuprofen", 0.8, 0)

print(str(script1))
print(repr(script1))
print(script1 + script2)
print(script1 + 10)
print(script1 == script2)
print(bool(script1))
print(bool(script3))