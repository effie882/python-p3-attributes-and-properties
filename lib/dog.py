#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name: str = "Unknown", breed: str = "Unknown"):
        if not isinstance(name, str) or name == "" or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return

        self.name = name

        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed
