from . import utils

import sys
import os
import logging


class recipes_object(object):

    def __init__(self):
        pass


class Recipe(recipes_object):

    def __init__(self):
        pass


class Note(recipes_object):

    def __init__(self):
        pass


class RecipesAPI(object):
    
    def __init__(self, rfile_path):
        self.rfile_path = rfile_path


class LinuxRecipesAPI(RecipesAPI):

    def __init__(self, rfile_path):
        super(LinuxRecipesAPI, self).__init__(rfile_path)


class MacOSRecipesAPI(RecipesAPI):

    def __init__(self):
        super(MacOSRecipesAPI, self).__init__(rfile_path)


class WindowsRecipesAPI(RecipesAPI):

    def __init__(self):
        super(WindowsRecipesAPI, self).__init__(rfile_path)


_platform_apis = {
    'Windows': WindowsRecipesAPI,
    'MacOS': MacOSRecipesAPI,
    'Linux': LinuxRecipesAPI,
}

def RecipesAPIFactory():
    """
    :returns: An OS-specific instance of RecipesAPI
    """
    logger = logging.getLogger("recipes")

    homedir = os.path.expanduser('~')
    rfile_path = os.path.join(homedir, ".recipes")
    platform = utils.get_platform(rfile_path)
    
    if platform:
        return _platform_apis[platform](rfile_path)