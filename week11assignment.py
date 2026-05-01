from dataclasses import dataclass, field
from contextlib import contextmanager

class PetError(Exception):
    pass

@dataclass
class Pet:
    name: str
    species: str
    age: int
    _status: str = field(default="NEW", init=False)

    def __post_init__(self):
        if self.age <= 0:
            raise PetError(f"Invalid age for pet: {self.name}")
    @property
    def is_senior(self):
        return self.age > 8
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age}yrs) [{self._status}]"
    def __lt__(self, other):
        return self.age < other.age

class AdoptionChecker:
    def __init__(self, pets, allowed):
        self.pets = pets
        self.allowed = allowed
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.pets):
            raise StopIteration
        pet = self.pets[self.index]
        if pet.species in self.allowed:
            pet._status = "ADOPTABLE"
        else:
            pet._status = "ON HOLD"
        self.index += 1
        return pet

def adoption_report(checker):
    adoptable = 0
    on_hold = 0
    for pet in checker:
        if pet._status == "ADOPTABLE":
            adoptable += 1
        else:
            on_hold += 1
        yield str(pet)
    yield f"Report: {adoptable} adoptable, {on_hold} on hold"

@contextmanager
def shelter_session(name):
    pets = []
    print(f">>> Intake: {name}")

    try:
        yield pets
    except PetError as error:
        print(f"!!! Error: {error}")
    finally:
        print(f"<<< Done: {name} ({len(pets)} pets)")

with shelter_session("Monday Batch") as pets:
    pets.append(Pet("Bella", "Dog", 3))
    pets.append(Pet("Milo", "Cat", 7))
    pets.append(Pet("Koko", "Parrot", 2))

    for line in adoption_report(AdoptionChecker(pets, ("Dog", "Cat"))):
        print(line)

    print(pets[0] < pets[1])

print()

with shelter_session("Tuesday Batch") as pets:
    pets.append(Pet("Rex", "Dog", -1))
