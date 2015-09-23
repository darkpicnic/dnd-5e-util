import yaml
import random
import constants


def generate_name(race, gender):
    """ Create a first and last name for character
    """
    normalized_race = race.lower()
    stream = file('data/names/{}.yaml'.format(normalized_race), 'r')
    data = yaml.load(stream)

    first = random.choice(data[gender.lower() + '_first_names'])
    last = random.choice(data['last_names'])

    return first, last
