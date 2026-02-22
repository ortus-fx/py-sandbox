import functools

import pandas as pd

group_ls = [
    "Salma Godiya Issifu",
    "Judith William",
    "Esther Ewurabena Appiah",
    "Gloria Mirekuaa Koranteng",
    "Priscilla Chidimma Nwachukwu",
    "Maame Yaa Akoto-Sampong",
    "Joycelyn Wesoamo Tigawoti",
    "Vanessa Bedzra",
    "Ivy Amexo",
    "Cameron Akorfa Harley",
    "Paula Manye Herzuah",
    "Joyce Yirenkyiwaa Ankomah",
    "Eugenia Darkoa Robertson",
    "Ernestina Akua Agyakuma Baidoo",
    "Justina Grace Attah Akweh",
    "Barzicia Oku",
    "Selasi Adzo Butu",
    "Georgette Kweiki Narh",
    "Sandra Osei",
    "Tryphena Ofori-Nyarko",
    "Florence Owusu Aduomi",
    "Mark Mawuli Kwaku Aguadze ",
    "Amos Kobina Mensah ",
    "Ohene Kwame Fredua",
    "Mohammed Abdulai",
    "Dominic Kwasi Appiah",
    "Solomon Yenyenle",
    "Gideon Cobbina",
    "Lawrence Williams",
    "Abdul Wahab Osman",
    "DESMOND KPONYO",
    "Elikem Kwame Dzakpasu",
    "Ramatu Mensah",
    "Abdul-malik Aduata Sumailah",
    "MICHAEL ABISSATH",
]


def first_lastname(func):
    @functools.wraps(func)
    def wrapper(*arg, **kwarg) -> pd.Series:
        grp_ls = func(*arg, *kwarg)
        grp_split = grp_ls.str.split()
        return (grp_split.str[0] + " " + grp_split.str[-1]).astype(dtype="string")

    return wrapper
