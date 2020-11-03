import re
from collections import namedtuple

from techtest.exceptions import MapError


Square = namedtuple('Square', ['x', 'y', 'size'])


def parse_metadata(line):
    '''
    Parses the first line of a map file
    The line follows the following format:

    10.ox

    - number of lines in the file
    - empty character
    - obstacle character
    - full character

    :param line: A line following the specified format
    :type line: str
    :returns: number of lines, empty, obstacle, full
    :rtype: tuple[Union(str, int)]
    '''
    parse_re = re.compile(r'(\d+?)(.)(.)(.)$')
    match = parse_re.search(line)
    return int(match.group(1)), match.group(2), match.group(3), match.group(4)


def check_map_valid(metadata, map):
    n_lines, empty, obstacle, full = parse_metadata(metadata)
    if not map or not n_lines:
        raise MapError('map needs at least one line of at least one cell')
    if len(map) != n_lines:
        raise MapError('number of lines do not match')
    line_length = len(map[0])
    if any(len(line) != line_length for line in map):
        raise MapError('line length are not consistent')

    # Concatenation of the map
    # Replace every instance of the description characters with an empty string
    # That way, if anything is left over, we know there are illegal characters
    # in the file
    concat = (
        ''.join(map)
        .replace(empty, '')
        .replace(obstacle, '')
        .replace(full, '')
    )
    if concat:
        raise MapError(
            (
                'map can only have characters as presented in the '
                'first line of the file'
            )
        )


def no_obstacles(map, obstacle, x_start, x_end, y_start, y_end):
    '''
    Function that checks that a section of the map doesn't have an
    obstacle

    :param map: the full map
    :type map: list[str]
    :param obstacle: The obstacle character, defined y the metadata
    :type obstacle: str
    :param x_start: The x-index to start the slice at
    :type x_start: int
    :param x_end: the x-index to end the slice at
    :type x_end: int
    :param y_start: the y-index to start the slice at
    :type y_start: int
    :param y_end: the y-index to end the slice at
    :type y_end: int
    :return: Whether or not there is an obstacle in the submap delimited
    by x_start, y_start and x_end, y_end
    :rtype: bool
    '''
    if x_end > len(map[0]) or y_end > len(map):
        # To simplify, we can imagine that the map is suurrounded by a wall
        # of obstacles.
        # The condition checks if we're out of bounds on x+ or y+
        # Checking for x- or y- is useless because the algorithm starts at
        # 0, 0 and grows the squares in the positive direction
        return False
    submap = [line[x_start:x_end] for line in map[y_start:y_end]]
    concat = ''.join(submap)
    return obstacle not in concat


def find_squares(filepath):
    '''
    Finds the squares in a given file

    :param filepath: The path to the file to find squares in
    :type filepath: str or pathlib.Path

    :raises: techtest.MapError if the map is invalid

    :returns: list of lines in the file, with squares marked appropriately
    :rtype: list[str]
    '''

    # read the file, and separate the
    # map from the first line (which is metadata)
    with open(filepath, 'r') as f:
        map = [line.strip('\n') for line in f]
        metadata = map.pop(0)

    # Will raise MapError according to the rules of the game
    check_map_valid(metadata, map)
    n_lines, empty, obstacle, full = parse_metadata(metadata)

    # We initialize an empty squares list to hold all the possible squares
    squares = []
    max_square_size = min(len(map[0]), n_lines)

    # We find all possible squares on that map, and if that square is valid
    # (no obstacles), we add it.
    for n in range(1, max_square_size + 1):
        for i, line in enumerate(map):
            for j, cell in enumerate(line):
                if no_obstacles(map, obstacle, i, i + n, j, j + n):
                    squares.append(Square(i, j, n))

    # We initialize our solution to be a square of size 0
    # its location doesn't matter
    solution = Square(0, 0, 0)

    # Then go through every possible square, in reverse, since they
    # are ordered from smallest to biggest
    for square in reversed(squares):
        if square.size >= solution.size:
            solution = square
        else:
            break

    # Then replace the map's tokens with the full token for each cell the
    # square occupies.
    map_solved = [list(line) for line in map]
    for y in range(solution.size):
        for x in range(solution.size):
            map_solved[solution.y + y][solution.x + x] = full
    return [''.join(lst) for lst in map_solved]
