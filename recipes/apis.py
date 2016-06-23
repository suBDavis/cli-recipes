from . import utils

import sys
import os
import logging


class RecipesAPI(object):
    
    def __init__(self, homedir, rfile_path, config):
        self.homedir = homedir
        self.rfile_path = rfile_path
        self.config = config
        self.recipe_list = []

    def build_from_config():
        self.recipe_list = utils.get_aliases_from_config(self.rfile_path)


class BashRecipesAPI(RecipesAPI):

    def __init__(self, homedir, rfile_path, config):
        super(BashRecipesAPI, self).__init__(homedir, rfile_path, config)
        self.profile_path = os.path.join(self.homedir, '.bashrc')

    def install(self):
        self.build_from_config()
        for recipe in self.recipe_list:
            self._put_recipe(recipe)

    def uninstall(self):
        pass

    def _put_recipe(self, recipe_text):
        with open(self.profile_path, 'w') as profile:
            pass


def RecipesAPIFactory(rfile_path=None):
    """
    :returns: An OS-specific instance of RecipesAPI
    """
    logger = logging.getLogger("recipes")

    homedir = os.path.expanduser('~')
    rfile_path = os.path.join(homedir, ".recipes") if rfile_path is None else rfile_path
    config = utils.load_from_config(rfile_path)

    if config['platform'] == 'linux' and config['shell'] == 'bash':
        return BashRecipesAPI(homedir, rfile_path, config)
    else:
        return BashRecipesAPI(homedir, rfile_path, config)