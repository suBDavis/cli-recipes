from recipes import RecipesAPI

import argparse
import sys
import logging


def parse_args(args):
    parser = argparse.ArgumentParser(description='Recipes - Manage Bash Aliases')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--install', action='store_true',
        help="install recipes for the working directory")
    group.add_argument('-u', '--uninstall', action='store_true',
        help="uninstall recipes for the working directory")
    group.add_argument('-a', '--add', dest='recipe_name', type=str, 
        help="create a new recipe and install it")
    parser.add_argument('-f', '--config', dest="recipes_file", type=str, default=None,
        help="path of the recipe config file")
    parser.add_argument('-v', '--verbose', action='store_true',
        help="enable verbose logging")
    parser.add_argument('-s', '--shell', dest='shell', type=str,
        help="name of the shell you use, if not bash.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args(sys.argv[1:])
    
    if args.verbose:
        logging.getLogger("recipes").setLevel(logging.DEBUG)
    
    recipe_manager = RecipesAPI(rfile_path=args.recipes_file)
    
    if args.install:
        recipe_manager.install()
    elif args.uninstall:
        recipe_manager.uninstall()
    elif args.recipe_name:
        pass