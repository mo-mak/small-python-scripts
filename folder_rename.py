import os, sys

folders_list = []
converted_names = []

def hyphenize(item):
    """ 
    this function will loop through every letter of the name 
    if there is a underscroe, it will be replaced with a hyphen
    """
    new_name = ''
    for letter in item: 
        if letter == '_':
            new_name += "-"
        else:
            new_name += letter
    return new_name

for folder in os.listdir():
    if os.path.isdir(folder):
        os.rename(folder,hyphenize(folder))
