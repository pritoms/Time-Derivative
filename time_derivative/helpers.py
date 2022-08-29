#!/usr/bin/env python3

import os
import termcolor


def get_config(config_file):
    config = {}
    with open(config_file) as f:
        config = json.load(f)
    return config


def get_path():
    return os.path.abspath(os.curdir)


def get_output_format(args):
    if args.format is not None:
        return args.format
    else:
        path = get_path()
        config_file = os.path.join(path, CONFIG_FILE)
        if os.path.isfile(config_file):
            config = get_config(config_file)
            return config['format']
        else:
            return OUTPUT_FORMAT


def get_color(args):
    if args.no_color:
        return False
    else:
        path = get_path()
        config_file = os.path.join(path, CONFIG_FILE)
        if os.path.isfile(config_file):
            config = get_config(config_file)
            return config['color']
        else:
            return COLOR


def get_heading(args):
    if args.no_heading:
        return False
    else:
        path = get_path()
        config_file = os.path.join(path, CONFIG_FILE)
        if os.path.isfile(config_file):
            config = get_config(config_file)
            return config['heading']
        else:
            return HEADING


def get_decoration(args):
    if args.no_decoration:
        return False
    else:
        path = get_path()
        config_file = os.path.join(path, CONFIG_FILE)
        if os.path.isfile(config_file):
            config = get_config(config_file)
            return config['decoration']
        else:
            return DECORATION


def get_json_file():
    path = get_path()
    json_file = os.path.join(path, JSON_FILE)
    if not os.path.isfile(json_file):
        print('Error: File \'' + json_file + '\' doesn\'t exist. Please run \'time_derivatives\' first.')
        exit()
    return json_file


def get_color_code(color):
    if color == 'red':
        return '\033[91m'
    elif color == 'green':
        return '\033[92m'
    elif color == 'yellow':
        return '\033[93m'
    elif color == 'blue':
        return '\033[94m'
    elif color == 'magenta':
        return '\033[95m'
    elif color == 'cyan':
        return '\033[96m'
    else:
        return ''


def colorize(string, color):
    if not COLOR:
        return string

    if color == 'red':
        return termcolor.colored(string, 'red')
    elif color == 'green':
        return termcolor.colored(string, 'green')
    elif color == 'yellow':
        return termcolor.colored(string, 'yellow')
    elif color == 'blue':
        return termcolor.colored(string, 'blue')
    elif color == 'magenta':
        return termcolor.colored(string, 'magenta')
    elif color == 'cyan':
        return termcolor.colored(string, 'cyan')
    else:
        return string


def generate_output(changes, output_format):
    if output_format == 'text':
        return generate_text_output(changes)
    elif output_format == 'html':
        return generate_html_output(changes)


def generate_text_output(changes):
    output = ''
    if HEADING:
        output += '\n'
        output += 'File Type'.ljust(16) + '| ' + 'Filename'.ljust(32) + '| ' + 'Action'.ljust(8) + '\n'
        output += '-' * 16 + '+' + '-' * 32 + '+' + '-' * 8 + '\n'
    for change in changes:
        output += change['file_type'].ljust(16) + '| ' + change['filename'].ljust(32) + '| ' + change['action'].ljust(8) + '\n'
    return output


def generate_html_output(changes):
    pass


def get_heading_row(table, heading, color):
    if HEADING:
        return table.add_row().add_cell(heading, colspan=2).set_style('background-color:' + color + '; font-weight: bold')
    else:
        return None


def get_line_separator(table, row, colspan):
    if DECORATION:
        return table.add_row().add_cell('', colspan=colspan).set_style('border-top: 1px solid black')
    else:
        return None
