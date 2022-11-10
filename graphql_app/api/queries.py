from .models import Person, Address
from ariadne import convert_kwargs_to_snake_case

def getPerson_resolver(obj, info):
    person = Person.query.get(1)
    
    return person.to_dict()

def getAddress_resolver(post, info):
    address = Address.query.get(1)

    return address.to_dict()