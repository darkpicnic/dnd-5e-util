import random
import constants

HUMAN_MALE_FIRST_NAMES = (
    "John", "William", "Garreth", "Jared"
)

HUMAN_FEMALE_FIRST_NAMES = (
    "Agatha", "Elizabeth", "Jane", "Roberta"
)

HUMAN_LAST_NAMES = (
    "Blackstone", "Crownsmith"
)

ELF_MALE_FIRST_NAMES = (
    "Adran",
    "Aelar",
    "Aust",
    "Beiro",
    "Heian",
)

ELF_FEMALE_FIRST_NAMES = (
    "Adrie",
    "Althaea",
    "Anastrianna",
    "Drusilia",
    "Lia",
)

ELF_LAST_NAMES = (
    "Amakiir",
    "Amastacia",
    "Siannodel",
)


def generate_name(race, gender):
    """ Create a first and last name for character
    """
    normalized_race = race.lower()
    if normalized_race == constants.ELF:
        first = random.choice(ELF_MALE_FIRST_NAMES) if gender == constants.MALE \
        else random.choice(ELF_FEMALE_FIRST_NAMES)
        last = random.choice(ELF_LAST_NAMES)
    elif normalized_race == constants.HUMAN:
        # TODO Finish
        first = random.choice(HUMAN_MALE_FIRST_NAMES) if gender == constants.MALE \
        else random.choice(HUMAN_FEMALE_FIRST_NAMES)
        last = random.choice(HUMAN_LAST_NAMES)
    return first, last
