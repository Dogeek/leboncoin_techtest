import argparse

from techtest import (
    __prog__, __version__, __author__,
    find_squares, MapError,
)


def get_version():
    return f'{__prog__} by {__author__} v{__version__}'


def main():
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
            print(str(e))


if __name__ == '__main__':
    main()
