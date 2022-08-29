#!/usr/bin/env python3
import os
import sys
import time
import json
from termcolor import colored, cprint

class TimeDerivative:
    def __init__(self, directory_old, directory_new, contents_old, contents_new):
        self.directory_old = directory_old
        self.directory_new = directory_new
        self.contents_old = contents_old
        self.contents_new = contents_new

    def display(self):
        # Get the arguments
        try:
            format = sys.argv[sys.argv.index('--format') + 1]
        except ValueError:
            format = 'text'
        except IndexError:
            print('Usage: {} --format FORMAT'.format(os.path.basename(sys.argv[0])), file=sys.stderr)
            return 1
        if format not in ['text', 'html']:
            print('{}: invalid output format'.format(format), file=sys.stderr)
            return 1
        try:
            color = sys.argv.index('--no-color') == -1
        except ValueError:
            color = True
        try:
            heading = sys.argv.index('--no-heading') == -1
        except ValueError:
            heading = True
        try:
            decoration = sys.argv.index('--no-decoration') == -1
        except ValueError:
            decoration = True

        # Get the differences between the old directory listing and the new one
        diff_old = set(self.contents_old) - set(self.contents_new)
        diff_new = set(self.contents_new) - set(self.contents_old)

        # Display the changes in text or HTML format
        if format == 'text':
            self.display_text(diff_old, diff_new, color, heading, decoration)
        elif format == 'html':
            self.display_html(diff_old, diff_new, color, heading, decoration)

    def display_text(self, diff_old, diff_new, color, heading, decoration):
        # Display the heading row
        if heading:
            print('{} {}'.format(colored('Old', 'yellow') if color else 'Old', colored('New', 'green') if color else 'New'))

        # Display the decorations
        if decoration:
            print(colored('-' * (len(self.directory_old) + len(self.directory_new) + 2), 'grey') if color else '-' * (len(self.directory_old) + len(self.directory_new) + 2))

        # Display the changes
        for entry in diff_old:
            print('{} {}'.format(colored(entry, 'yellow') if color else entry, ''))
        for entry in diff_new:
            print('{} {}'.format('', colored(entry, 'green') if color else entry))

    def display_html(self, diff_old, diff_new, color, heading, decoration):
        # Display the head section
        print('<!DOCTYPE html>')
        print('<html lang="en">')
        print('<head>')
        print('<meta charset="utf-8">')
        print('<title>Time Derivatives</title>')
        print('<style type="text/css">')
        print('table { border-collapse: collapse; }')
        print('td { padding: 0.25em 0.5em; border: 1px solid black; }')
        print('td.old { background-color: #ffd700; }')
        print('td.new { background-color: #008000; }')
        print('</style>')
        print('</head>')

        # Display the body section
        print('<body>')

        # Display the heading row
        if heading:
            print('<table>')
            print('<tr>')
            print('<td class="old">Old</td>')
            print('<td class="new">New</td>')
            print('</tr>')

        # Display the decorations
        if decoration:
            print('<tr>')
            print('<td colspan="2" style="background-color: #808080;"></td>')
            print('</tr>')

        # Display the changes
        for entry in diff_old:
            print('<tr>')
            print('<td class="old">{}</td>'.format(entry))
            print('<td class="empty"></td>')
            print('</tr>')
        for entry in diff_new:
            print('<tr>')
            print('<td class="empty"></td>')
            print('<td class="new">{}</td>'.format(entry))
            print('</tr>')

        # Display the closing tags
        if heading:
            print('</table>')
        print('</body>')
        print('</html>')
