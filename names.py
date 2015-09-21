import random

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
    first = random.choice(ELF_MALE_FIRST_NAMES) if gender == "male" else random.choice(ELF_FEMALE_FIRST_NAMES)
    last = random.choice(ELF_LAST_NAMES)
    return first, last
