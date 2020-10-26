"""sqlalchemy/queries.py"""

from model import Human, Animal, connect_to_db, db
from flask import Flask

app = Flask(__name__)
connect_to_db(app)

# Get the human with the primary key 2
query_1 = Human.query.filter(Human.fname=='Jane', Human.human_id ==2).all()
print(query_1)

# Get the first animal whose species is "fish"
query_2 = Animal.query.filter(Animal.animal_species=='fish',Animal.name=='Bubbles').first()
print(query_2)

# Get all the animals with who belong to the human
# with primary key 5
query_3 = Animal.query.filter(Animal.human_id == 5).all()
print(query_3)


# Get all animals born in a year greater than (but not equal to) 2015.
query_4 = Animal.query.filter(Animal.birth_year >2015).all()
print(query_4)

# Get all the humans with first names that start with "J"
query_5 = Human.query.filter(Human.fname.like('J%')).all()
print(query_5)



# Get all the animals who don't have a birth year
query_6 = Animal.query.filter(Animal.birth_year ==None).all()
print(query_6)

# Get all the animals with species "fish" OR "rabbit"

query_7 = Animal.query.filter(Animal.animal_species.in_(['fish' , 'rabbit'])).all()
print(query_7)

# Get all the humans who don't have an email address that
# contains "gmail"
query_8 = Human.query.filter(Human.email.notlike('%gmail%')).all()
print(query_8)



#
# Continue reading the instructions before you move on!
#


def print_humans_and_animals():
    """Print a directory of humans and their animals"""
    query_humans = Human.query.all()
    for id in query_humans:
        print(id.fname, id.lname)
        pets = Animal.query.filter(Animal.human_id==Human.human_id).all()
        for a_id in pets:
            print('-',a_id.name,",",a_id.animal_species)
print_humans_and_animals()




def get_humans_by_animal_species(animal_species):
    """Return a list of Human objects who have animals of a certain species.

    The returned list doesn't have duplicates.

    Args:
        - animal_species: an animal's species.

    """

    query_humans = Human.query.all()
    humans_list = []
    for id in query_humans:
        
        pets = Animal.query.filter(Animal.human_id==Human.human_id).all()
        for pet_id in pets:
            if(pet_id.animal_species==Animal.animal_species):
                if (id not in humans_list):
                    humans_list.append(id)
    return humans_list  
                