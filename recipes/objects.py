from . import utils

import sys

class recipe_object(object):

    def __init__(self):
        pass


class Recipe(recipe_object):

    def __init__(self):
        pass


class Note(recipe_object):

    def __init__(self):
        pass


class RecipesAPI(object):
    
    def __init__(self):
        pass


class LinuxRecipesAPI(RecipesAPI):

    def __init__(self):
        pass


class MacOSRecipesAPI(RecipesAPI):

    def __init__(self):
        pass


class WindowsRecipesAPI(RecipesAPI):

    def __init__(self):
        pass


def RecipesAPIFactory():
    """
    :returns: An OS-specific instance of RecipesAPI
    """
    if sys.platform == "win32":
        return WindowsRecipesAPI()
    elif sys.platform == "darwin":
        return MacOSRecipesAPI()
    else:
        # Linux, Cygwin, etc.
        return LinuxRecipesAPI()