class MapError(Exception):
    '''
    Error raised when the map file is not conform to the
    specified format.

    The format should be:
        - every line should have the same length
        - there is at least one line of at least one cell
        - each line ends with a newline (`\n`)
        - the map can only have characters as presented
          on the first line of the file
    '''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return f'MapError : {self.message}'
