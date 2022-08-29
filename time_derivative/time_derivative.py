#!/usr/bin/env python3

import argparse
import json
import os


def get_args():
    parser = argparse.ArgumentParser(description='Display the changes that happened in a directory over the course of time.')
    parser.add_argument('-f', '--format', help='output format (default: text)', choices=['text', 'html'])
    parser.add_argument('--no-color', action='store_true', help='disable color output')
    parser.add_argument('--no-heading', action='store_true', help='disable heading row')
    parser.add_argument('--no-decoration', action='store_true', help='disable decorations')
    args = parser.parse_args()
    return args


def load_json_file(json_file):
    with open(json_file) as f:
        file_listings = json.load(f)
    return file_listings


def compare_files(previous_listing, current_listing):
    previous_filenames = [x['filename'] for x in previous_listing]
    current_filenames = [x['filename'] for x in current_listing]

    added_files = list(set(current_filenames) - set(previous_filenames))
    deleted_files = list(set(previous_filenames) - set(current_filenames))

    changes = []

    for filename in added_files:
        file = [x for x in current_listing if x['filename'] == filename][0]
        changes.append({'file_type': file['file_type'], 'filename': file['filename'], 'action': 'added'})

    for filename in deleted_files:
        file = [x for x in previous_listing if x['filename'] == filename][0]
        changes.append({'file_type': file['file_type'], 'filename': file['filename'], 'action': 'deleted'})

    return changes


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


def main():
    args = get_args()
    OUTPUT_FORMAT = get_output_format(args)
    COLOR = get_color(args)
    HEADING = get_heading(args)
    DECORATION = get_decoration(args)

    json_file = get_json_file()
    file_listings = load_json_file(json_file)
    changes = compare_files(file_listings['previous'], file_listings['current'])
    if len(changes) > 0:
        print(generate_output(changes, OUTPUT_FORMAT))
    else:
        print('No changes detected.')


if __name__ == '__main__':
    main()
