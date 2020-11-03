import argparse
import sys

from techtest import (
    __prog__, __version__, __author__,
    find_squares, MapError,
)


def get_version():
    '''
    Returns the program name, its author and the version number
    in a formatted string

    :return: A string with the program name, its author, and the version number
    :rtype: str
    '''
    return f'{__prog__} by {__author__} v{__version__}'


def main():
    '''
    Main function of the CLI. Creates the parser, and sends each
    filepath to the find_squares function
    '''
    parser = argparse.ArgumentParser(prog=__prog__)
    parser.add_argument(
        '--version', '-V', action='version',
        version=get_version(),
    )
    parser.add_argument(
        'filepaths', nargs='+', type=str,
        help='Filenames for which to find squares in.',
    )
    args = parser.parse_args()
    for filepath in args.filepaths:
        try:
            print('\n'.join(find_squares(filepath)))
        except MapError as e:
            print(str(e), file=sys.stderr)


if __name__ == '__main__':
    main()
