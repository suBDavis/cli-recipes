import logging
import sys
import os

_comment_char = '#'

def export_to_rfile():
    pass

def get_platform(rfile_path):

    logger = logging.getLogger("recipes")

    try:
        with open(rfile_path, 'r') as rfile:
            platform = get_platform_from_rfile(rfile)
    except FileNotFoundError:
        platform = (
            "Windows" if sys.platform == "win32" else
            "MacOS" if sys.platform == "darwin" else
            "Linux")
        print("Your platform was determined as %s" % platform)
        print("Other options are:"
              "\n1) Windows"
              "\n2) MacOS"
              "\n3) linux"
              "\nEnter a number to contine, or press enter to accept defaults.")
        key = input()
        if len(key) == 1:
            platform = (
                "Windows" if key is "1" else
                "MacOS" if key is "2" else
                "Linux")
        print("Platform Selected: %s" % platform)
    except Exception as e:
        logger.error("Unexpected Exception %s" % e)
        exit(1)

    return platform


def get_platform_from_rfile(file):
    for line in rfile.readline():
        if not is_comment(line):
            print(line)


def is_comment(line_string):
    line_string = line_string.trim()
    if line_string[0] is comment_char:
        return true
    else:
        return false