from App.Objects.Object import Object
from typing import Any

class Response(Object):
    '''
    Wrapper for responses from Executable. Must be extended with unique field

    class fields must not be used directly.

    Abstract methods:

    fromItems() - create class instance from data

    To JSON:

    to_json()
    '''

    @staticmethod
    def fromItems(items):
        '''
        Allows to create Response without constructor
        '''
        pass
