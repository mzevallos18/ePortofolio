# seed_animals.py
# Insert ~20 sample breeds (dogs + cats) into aac.animals using your AnimalShelter wrapper.

from animalshelter import AnimalShelter

# Adjust if you’re using username/password or a connection string
db = AnimalShelter()  # default: localhost:27017, db=aac, coll=animals

docs = [
    # ---- Dogs (10) ----
    {"animal_type": "Dog", "breed": "Labrador Retriever", "age_upon_outcome": "2 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "German Shepherd", "age_upon_outcome": "3 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "Golden Retriever", "age_upon_outcome": "1 year", "sex_upon_outcome": "Intact Male", "outcome_type": "Transfer"},
    {"animal_type": "Dog", "breed": "French Bulldog", "age_upon_outcome": "8 months", "sex_upon_outcome": "Intact Female", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "Bulldog", "age_upon_outcome": "4 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "Poodle", "age_upon_outcome": "2 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "Beagle", "age_upon_outcome": "3 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "Rottweiler", "age_upon_outcome": "5 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Transfer"},
    {"animal_type": "Dog", "breed": "Dachshund", "age_upon_outcome": "1 year", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Dog", "breed": "German Shorthaired Pointer", "age_upon_outcome": "2 years", "sex_upon_outcome": "Intact Male", "outcome_type": "Adoption"},

    # ---- Cats (10) ----
    {"animal_type": "Cat", "breed": "Domestic Shorthair", "age_upon_outcome": "3 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Domestic Medium Hair", "age_upon_outcome": "2 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Domestic Longhair", "age_upon_outcome": "6 months", "sex_upon_outcome": "Intact Female", "outcome_type": "Transfer"},
    {"animal_type": "Cat", "breed": "Siamese", "age_upon_outcome": "4 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Maine Coon", "age_upon_outcome": "5 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Ragdoll", "age_upon_outcome": "2 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Bengal", "age_upon_outcome": "1 year", "sex_upon_outcome": "Intact Male", "outcome_type": "Transfer"},
    {"animal_type": "Cat", "breed": "Sphynx", "age_upon_outcome": "3 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "British Shorthair", "age_upon_outcome": "2 years", "sex_upon_outcome": "Neutered Male", "outcome_type": "Adoption"},
    {"animal_type": "Cat", "breed": "Persian", "age_upon_outcome": "7 years", "sex_upon_outcome": "Spayed Female", "outcome_type": "Transfer"},
]

inserted = 0
for d in docs:
    # avoid duplicates by (animal_type, breed)
    exists = db.read({"animal_type": d["animal_type"], "breed": d["breed"]}, limit=1)
    if exists and next(exists, None):
        continue
    if db.create(d):
        inserted += 1

print(f"Inserted {inserted} new documents.")
