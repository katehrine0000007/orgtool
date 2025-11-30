from App.Objects.Object import Object
from typing import Any

class Response(Object):
    '''
    class fields must not be used directly
    '''

    def toDict(self) -> Any:
        '''
        Returns data in json serializable format
        '''
        return self.data

    def toData(self) -> Any:
        pass

    @staticmethod
    def fromItems(items):
        '''
        Allows to create Response without constructor
        '''
        pass
