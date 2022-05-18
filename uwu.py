import random

"""Credit goes to
https://github.com/python-discord/sir-lancebot/commit/0794f26ea267c355e106366a1226f3e986a682fc
"""
UWU_WORDS = {
    "fi": "fwi",
    "l": "w",
    "r": "w",
    "some": "sum",
    "th": "d",
    "thing": "fing",
    "tho": "fo",
    "you're": "yuw'we",
    "your": "yur",
    "you": "yuw",
}

def uwufied(text, stuttering):
    converted = text

    """ This first converts based from Uwu_Words"""
    for curr in UWU_WORDS.keys():
        converted = converted.replace(curr, UWU_WORDS[curr])
    
    stuterring_converted = ""

    """Given a percentage, we'll determine if we add a stutter or not"""
    for curr in converted.split(' '):
        random_num = random.uniform(0, 1)
        if (random_num<=stuttering):
            first_char = curr[0]
            replaced = curr.replace(first_char,first_char+"-"+first_char.lower(),1)
            stuterring_converted = stuterring_converted + replaced + " "
        else:
            stuterring_converted = stuterring_converted + curr + " "


    # print(text.translate(str.maketrans(''.join(UWU_WORDS.keys()), ''.join(UWU_WORDS.values()))))
    print(stuterring_converted)
    return stuterring_converted