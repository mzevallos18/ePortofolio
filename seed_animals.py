# Import the AnimalShelter class from the animalshelter module
from animalshelter import AnimalShelter

db = AnimalShelter()

# Define a list of documents (each document represents an animal record)
# Each record includes details such as animal type, breed, age, sex, and outcome type
docs = [
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

# Initialize a counter to keep track of how many new records were inserted
inserted = 0

# Loop through each document in the list
for d in docs:
    # Check if a record with the same animal_type and breed already exists in the database
    exists = db.read({"animal_type": d["animal_type"], "breed": d["breed"]}, limit=1)
    
    # If the record already exists, skip it to avoid duplicates
    if exists and next(exists, None):
        continue
    
    # Otherwise, create (insert) a new record in the database
    if db.create(d):
        inserted += 1  # Increment counter when successful

# Print out how many new records were added to the database
print(f"Inserted {inserted} new documents.")
