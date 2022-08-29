# Time Derivative

This script is used to display the changes that happened in a directory over the course of time. It will read the `time_derivatives.json` file, which can be created using the `time_derivatives.py` script, and display the differences between the previous directory listing and the current one.

## Usage

```bash
$ time_derivative.py --help
usage: time_derivative.py [-h] [--format {text,html}] [--no-color]
                          [--no-heading] [--no-decoration]
                          JSON_FILE

Display the changes that happened in a directory over the course of time.

positional arguments:
  JSON_FILE             JSON file containing the directory listings

optional arguments:
  -h, --help            show this help message and exit
  --format {text,html}  output format (default: text)
  --no-color            disable color output
  --no-heading          disable heading row
  --no-decoration       disable decorations
```

## Examples

```bash
$ time_derivatives.py time_derivatives.json /tmp/test/
$ time_derivatives.py time_derivatives.json /tmp/test/
$ time_derivative.py time_derivatives.json
Old                     New
------------------------
file1                   file2
file3                   file4
$ time_derivative.py --format html time_derivatives.json > test.html
```

## Installation

```bash
$ make
$ sudo make install
```

## Compatibility

This script is compatible with Python 3.2 and above.

## License

The MIT License (MIT)
Copyright (c) 2018 Pritoms

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
