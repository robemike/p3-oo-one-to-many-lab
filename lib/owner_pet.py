class Owner:
    def __init__(self, name):
        self.name = name 

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda p: p.name)

class Pet:

    all = list()

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner = None):
        self.name = name 
        if pet_type not in self.PET_TYPES:
            raise Exception
        self.pet_type = pet_type 
        self.owner = owner 
        Pet.all.append(self)

