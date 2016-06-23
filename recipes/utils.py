from . import objects

import logging
import sys
import os
import json
import ntpath

_comment_char = '#'
_logger = logging.getLogger("recipes")


def export_to_rfile():
    pass


def load_from_config(rfile_path):
    if os.path.exists(rfile_path):
        try:
            rfile = open(rfile_path, 'r')
        except:
            _logger.error("Could not read from %s" % rfile_path)
        with rfile:
            return parse_rfile_json_header(rfile)
    else:
        initialize_rfile(rfile_path)
        return load_from_config(rfile_path)


def parse_rfile_json_header(rfile):
    json_string = ""
    
        clean_line = line.strip()
        if len(clean_line) is not 0:
            if clean_line[0] is _comment_char:
                break
            json_string += clean_line
    return json.loads(json_string)   


def initialize_rfile(rfile_path, platform="linux", shell="bash"):
    try:
        shell = ntpath.basename(os.environ['SHELL'])
    except:
        pass

    rfile_contents = {
        "platform": platform,
        "shell": shell.lower()
    }
    with open(rfile_path, 'w') as rfile:
        rfile.write(json.dumps(rfile_contents))

def get_aliases_from_config(rfile_path):
    aliases_list = []
    with open(rfile_path, 'r') as rfile:
        for line in rfile.readline():